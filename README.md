# hello_kubernetes
Demo requires access to a preset kubernetes cluster.

Raspberry pi cluster has been inspired by following blog entry:
https://kubecloud.io/setup-a-kubernetes-1-9-0-raspberry-pi-cluster-on-raspbian-using-kubeadm-f8b3b85bc2d1


# Docker
docker build -t optimodev/hellok8s:v1 .

docker run -d --name hellok8s -p 80:80 optimodev/hellok8s:v1

docker push optimodev/hellok8s:v1


# k8s
kubectl get nodes
kubectl get all --all-namespaces

kubectl create -f hellok8s-deployment.yaml
kubectl get deployments
kubectl get pods

kubectl create -f hellok8s-service.yaml
kubectl get svc

kubectl scale deployment hellok8s --replicaas=20
kubectl get pods

kubectl edit deployment hellok8s

