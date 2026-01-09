---
title: Podman Kube
nav_order: 5
---

# ☸️ Podman Kube  
Podman can **export containers and pods into Kubernetes YAML**, which means you can take a locally running app and deploy it to a Kubernetes cluster—without learning YAML from scratch.

This feature bridges the gap between **local container work** and **production Kubernetes** 🚀

---

## 🎯 Why Podman Kube?

| Task | Podman | Kubernetes |
|------|--------|------------|
| Build & run containers | ✔ Yes | ❌ No |
| Run multiple containers | ✔ Via Pods | ✔ Via Pods |
| Share networks | ✔ Yes | ✔ Yes |
| Deploy apps declaratively | ❌ Not with CLI | ✔ Yes |
| Convert workloads | ✔ `podman generate kube` | N/A |

Podman Kube gives you **the missing link**:
You design locally → Podman generates YAML → Kubernetes runs it.

---

## 🫙 Requirement: Pod Must Exist

Before generating YAML, create a Pod and add containers:

```bash
podman pod create --name mypod -p 8080:80
podman run -d --pod mypod nginx
podman run -d --pod mypod redis
```

Verify:
```bash
podman pod ps
```

---

## 📦 Generate Kubernetes YAML

Run:
```bash
podman generate kube mypod > pod.yaml
```

This creates a file like:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: nginx
    image: docker.io/library/nginx:latest
  - name: redis
    image: docker.io/library/redis:latest
```

🎉 You now have valid Kubernetes config!

---

## ▶️ Launch Using Podman Kube

Use the generated file:
```bash
podman kube play pod.yaml
```

Podman:
- reads the YAML
- creates the pod
- recreates all containers listed

Confirm:
```bash
podman pod ps
```

---

## 🔁 Redeploy After Editing YAML

Edit `pod.yaml`, then update deployment:
```bash
podman kube down pod.yaml
podman kube play pod.yaml
```

This gives you a **GitOps-like workflow** locally.

---

## 🛑 Remove Kubernetes Objects

Stop & remove containers defined by YAML:
```bash
podman kube down pod.yaml
```

---

## 🌍 Deploy to Real Kubernetes

Once YAML works locally, deploy it to a cluster:

Minikube:
```bash
kubectl apply -f pod.yaml
```

KIND:
```bash
kind create cluster
kubectl apply -f pod.yaml
```

Cloud:
```bash
kubectl apply -f pod.yaml
```

No changes required 🎉

---

## 📊 Architecture Flow

```
+-------------------+
| Podman Pod        |
| (local runtime)   |
+-------------------+
          |
   generate kube
          v
+-------------------+
| Kube YAML (pod)   |
| Deployable file   |
+-------------------+
          |
     kubectl apply
          v
+-------------------+
| Kubernetes Pod    |
| (cluster runtime) |
+-------------------+
```

---

## 🧩 Things Included in YAML

✔ pod name  
✔ container names  
✔ images & tags  
✔ ports  
✔ environment vars  
✔ mounts (if defined)

---

## 🚨 Things **Not** Included Automatically

❌ Volumes (unless specified)  
❌ Secrets  
❌ ConfigMaps  
❌ Deployment scaling  
❌ Services / LoadBalancer

But you can add them manually!

---

## 🎉 Summary Cheat Sheet

| Action | Command |
|--------|---------|
| Export Pod → YAML | `podman generate kube mypod > pod.yaml` |
| Run YAML | `podman kube play pod.yaml` |
| Stop | `podman kube down pod.yaml` |
| Deploy to cluster | `kubectl apply -f pod.yaml` |

---

## 🏁 You Learned
✔ Create pods locally  
✔ Generate Kubernetes-ready YAML  
✔ Deploy YAML back into Podman  
✔ Deploy YAML into real Kubernetes

➡ Next: Check **[Podman Compose](cheatsheet.md)** for fast reference!
