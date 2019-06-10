# Prometheus.

https://devopscube.com/setup-prometheus-monitoring-on-kubernetes/

kubectl create -f kubernetes-prometheus/clusterRole.yaml
kubectl create -f kubernetes-prometheus/config-map.yaml -n monitoring
kubectl create -f kubernetes-prometheus/prometheus-deployment.yaml -n monitoring
kubectl create -f kubernetes-prometheus/prometheus-service.yaml -n monitoring

# Go App.

https://medium.com/@zhimin.wen/custom-prometheus-metrics-for-apps-running-in-kubernetes-498d69ada7aa

kubectl create -f go_app.yaml

# Custom metrics and HPA.

https://itnext.io/horizontal-pod-autoscale-with-custom-metrics-8cb13e9d475

helm install --name adapter stable/prometheus-adapter --values custom-metrics/values.yaml
kubectl delete configmaps adapter-prometheus-adapter
kubectl create -f custom-metrics/config-map-custom-metrics.yaml
kubectl delete pods adapter-prometheus-adapter-*
kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq .
kubectl create -f hpa.yaml

# Test the hpa.

pip install -r requirements.txt
python main.py
