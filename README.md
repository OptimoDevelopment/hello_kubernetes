# hello_kubernetes

# Docker
docker build -t optimodev/hellok8s .

docker run -it --rm --name hellok8s -p 8077 optimodev/hellok8s

docker push optimodev/hellok8s


# k8s
kubectl get nodes
kubectl get all --all-namespaces

kubectl create -f hellok8s-deployment.yaml
kubectl get deployments

kubectl create -f hellok8s-service.yaml
kubectl get svc

kubectl scale deployment hellok8s --replicaas=20
kubectl get pods

kubectl edit deployment hellok8s

