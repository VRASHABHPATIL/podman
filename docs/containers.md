---
title: Containers
nav_order: 2
---

# 🐳 Working With Containers in Podman  
The complete guide to **running, managing, inspecting, networking and cleaning up containers** using Podman.

---

## 🔥 What Are Containers?

Containers are **lightweight, isolated environments** that run applications with:
- their own filesystem
- their own process space
- controlled CPU & memory usage

Unlike virtual machines, containers share the host kernel — making them **faster and smaller**.

---

## 🛒 Pull Images (Download From Registry)

Before running a container, download its base image:

```bash
podman pull nginx:latest
podman pull mysql:8
podman pull alpine
```

List local images:

```bash
podman images
```

---

## ▶️ Run Containers

Run a container in the background:

```bash
podman run -d -p 8080:80 nginx
```

Flags explained:
- `-d` → detached mode
- `-p HOST:CONTAINER` → publish port  
  e.g. host port `8080` → container port `80`

Check running containers:
```bash
podman ps
```

Run interactively (opens terminal inside container):
```bash
podman run -it alpine sh
```

Auto-remove container after exit:
```bash
podman run --rm alpine echo "Hello Podman"
```

---

## 🏷️ Naming Containers

Give containers friendly names:

```bash
podman run -d --name web nginx
```

Now use:
```bash
podman stop web
podman logs web
```

---

## 📜 Logs (Debugging)

```bash
podman logs web
podman logs -f web   # stream live logs
```

---

## 🧠 Inspect Containers

```bash
podman inspect web
```

Shows:
- Mounts
- Networks
- Ports
- Resources
- Entrypoint & command

---

## 🧪 Exec — Run Commands Inside a Container

Open a shell:
```bash
podman exec -it web bash
```

Or for small images:
```bash
podman exec -it web sh
```

---

## 📂 Working With Volumes (Persistent Data)

Mount local folder into container:
```bash
podman run -d \
  -v ./site:/usr/share/nginx/html \
  -p 8080:80 \
  nginx
```

Copy files:
```bash
podman cp web:/etc/nginx/nginx.conf .
podman cp myfile.txt web:/tmp/
```

---

## 🔐 Environment Variables

```bash
podman run \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8
```

---

## 🌐 Container Networking

### ⭐ Default Networking
Every rootless Podman container gets its own isolated network namespace.

Check network:
```bash
podman inspect web | grep -i ip
```

### 🌍 Expose Ports to Host
```bash
podman run -d -p 8080:80 nginx
```

### 🔗 Bridge Network Between Containers
Run 2 containers that can communicate:

```bash
podman network create mynet
podman run -d --name db --network mynet mysql:8 -e MYSQL_ROOT_PASSWORD=pass
podman run -it --name api --network mynet alpine sh
```

Inside `api`, test connectivity:
```bash
ping db
```

### ✔ Host Mode
Container uses host network stack:
```bash
podman run --net=host nginx
```

---

## 🌡️ Resource Monitoring

```bash
podman stats
```

Shows CPU %, memory, I/O per container

---

## 🔁 Stop / Restart / Remove Containers

Stop container:
```bash
podman stop web
```

Restart:
```bash
podman restart web
```

Remove:
```bash
podman rm web
```

Remove all stopped:
```bash
podman rm -a
```

---

## 🧹 System Cleanup

Remove unused images:
```bash
podman rmi -a
```

Free unused networks & caches:
```bash
podman system prune -a -f
```

---

## 🧱 Architecture Diagram — Single Container

```
+-----------------------+
|   Podman Engine       |
|   (No Daemon!)        |
+-----------+-----------+
            |
     Runs Container
            |
  +----------------------+
  |     nginx image      |
  |   read‑only layers   |
  +----------------------+
            |
   Published network port
            |
     localhost:8080 (host)
```

---

## 📌 Key Takeaways

| Action | Command |
|--------|---------|
| Pull image | `podman pull` |
| Run container | `podman run` |
| List containers | `podman ps` |
| Enter container | `podman exec -it` |
| Logs | `podman logs` |
| Network create | `podman network create` |
| Cleanup | `podman system prune` |

---

➡ Next: **[Pods](pods.md)** — multiple containers sharing the same namespace!
