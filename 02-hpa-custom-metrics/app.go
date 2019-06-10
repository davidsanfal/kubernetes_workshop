package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

type PrometheusHttpMetric struct {
	Prefix                string
	ClientConnected       prometheus.Gauge
	TransactionTotal      *prometheus.CounterVec
	ResponseTimeHistogram *prometheus.HistogramVec
	Buckets               []float64
}

var (
  latency = prometheus.NewHistogram(
     prometheus.HistogramOpts{
        Name:      "myapp_server_latency",
        Help:      "Latency",
     })
)

func InitPrometheusHttpMetric(prefix string, buckets []float64) *PrometheusHttpMetric {
	phm := PrometheusHttpMetric{
		Prefix: prefix,
		ClientConnected: promauto.NewGauge(prometheus.GaugeOpts{
			Name: prefix + "_client_connected",
			Help: "Number of active client connections",
		}),
		TransactionTotal: promauto.NewCounterVec(prometheus.CounterOpts{
			Name: prefix + "_requests_total",
			Help: "total HTTP requests processed",
		}, []string{"code", "method"},
		),
		ResponseTimeHistogram: promauto.NewHistogramVec(prometheus.HistogramOpts{
			Name:    prefix + "_response_time",
			Help:    "Histogram of response time for handler",
			Buckets: buckets,
		}, []string{"handler", "method"}),
	}

	return &phm
}

func (phm *PrometheusHttpMetric) WrapHandler(handlerLabel string, handlerFunc http.HandlerFunc) http.Handler {
	handle := http.HandlerFunc(handlerFunc)
	wrappedHandler := promhttp.InstrumentHandlerInFlight(phm.ClientConnected,
		promhttp.InstrumentHandlerCounter(phm.TransactionTotal,
			promhttp.InstrumentHandlerDuration(phm.ResponseTimeHistogram.MustCurryWith(prometheus.Labels{"handler": handlerLabel}),
				handle),
		),
	)
	return wrappedHandler
}

func myHandler(w http.ResponseWriter, r *http.Request) {
	cost := r.FormValue("cost")
	val, err := strconv.ParseFloat(cost, 64)
	if err != nil {
		http.Error(w, "Fail to convert cost as float value", 500)
		return
	}

	sleep := time.Duration(val*1e+9) * time.Nanosecond
	time.Sleep(sleep)
  latency.Observe(val)
	fmt.Fprintf(w, "Time spend for this request: %.2f", sleep.Seconds())
}

func main() {
  prometheus.MustRegister(latency)
	phm := InitPrometheusHttpMetric("myapp", prometheus.LinearBuckets(0, 5, 20))

	http.Handle("/metrics", promhttp.Handler())
	http.Handle("/service", phm.WrapHandler("myhandler", myHandler))

	port := os.Getenv("LISTENING_PORT")

	if port == "" {
		port = "8080"
	}
	log.Printf("listening on port:%s", port)

	err := http.ListenAndServe(":"+port, nil)
	if err != nil {
		log.Fatalf("Failed to start server:%v", err)
	}
}
