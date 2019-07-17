kubectl apply -f simple-api.yaml
helm install --name adapter stable/prometheus-adapter --values custom-metrics/values.yaml
kubectl delete configmaps adapter-prometheus-adapter
kubectl create -f custom-metrics/config-map-custom-metrics.yaml
kubectl delete --all pods --namespace=default
