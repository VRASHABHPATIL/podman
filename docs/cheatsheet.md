---
title: Podman Cheat Sheet
nav_order: 6
---

# 🧾 Podman Cheat Sheet  
Fast reference for **Podman CLI**, grouped by task.

---

## 🐳 Containers

### Run
```bash
podman run -d nginx
podman run -it alpine sh
podman run --rm alpine echo "hello"
```

### Inspect / Exec
```bash
podman ps -a
podman inspect <id>
podman logs -f <id>
podman exec -it <id> bash
```

### Stop & Remove
```bash
podman stop <id>
podman rm <id>
podman rm -a   # remove all stopped
```

---

## 🏗️ Images

### Pull & Build
```bash
podman pull nginx
podman build -t app -f Containerfile .
```

### Manage
```bash
podman images
podman rmi <image>
podman rmi -a   # remove all
```

---

## 🫙 Pods

### Create & Use
```bash
podman pod create --name mypod -p 8080:80
podman run -d --pod mypod nginx
podman ps --pod
```

### Manage
```bash
podman pod stop mypod
podman pod rm mypod
```

---

## 🤝 Podman Compose

### Start / Stop
```bash
podman-compose up -d
podman-compose down
```

### Logs & Exec
```bash
podman-compose logs -f
podman-compose exec web bash
```

---

## ☸️ Kube

### Convert & Apply
```bash
podman generate kube mypod > pod.yaml
podman kube play pod.yaml
podman kube down pod.yaml
```

---

## 🌐 Networking

### Port mapping
```bash
podman run -d -p 8080:80 nginx
```

### Create network
```bash
podman network create mynet
```

### Run on network
```bash
podman run -d --network mynet redis
```

---

## 📁 Volumes

```bash
podman volume create data
podman run -v data:/var/lib/mysql mysql
```

---

## 👀 Monitoring

```bash
podman ps
podman stats
podman top <id>
```

---

## 🧹 Cleanup

```bash
podman rm -a
podman rmi -a
podman system prune -a -f
```

---

## 🎉 Tip
`podman help <command>` shows flags for any subcommand.
