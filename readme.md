```
https://kubernetes.io/docs/tasks/tools/install-minikube/
minikube start
eval $(minikube docker-env)
minikube addons enable ingress
minikube tunnel
```

```
docker build -t domain domain/.
docker build -t front front/.
```

```
kubectl get pods
kubectl apply -f domain/deployment_v1.yaml
kubectl apply -f domain/service_node.yaml
minikube ip
curl <ip>:30037
```

```
kubectl apply -f domain/deployment_v2.yaml
kubectl apply -f domain/service_all.yaml
kubectl apply -f front/deployment.yaml
kubectl apply -f front/service_node.yaml
minikube ip
curl <ip>:30036

kubectl apply -f front/service_lb.yaml
kubectl get services
curl <ip>:5000

kubectl apply -f domain/service_v2.yaml
curl <ip>:5000
```

```
kubectl apply -f front/service.yaml
kubectl apply -f ingress.yaml
minikube ip
curl <ip>/front
```

```
kubectl get ...
kubectl apply ...
kubectl describe ...
kubectl edit ...
```
