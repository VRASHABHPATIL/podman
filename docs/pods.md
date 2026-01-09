---
title: Podman Pods
nav_order: 3
---

# 🫙 Podman Pods  
Pods allow **multiple containers to run together** and share resources — just like Kubernetes Pods.

In Podman, containers inside the same pod share:
✔ Network namespace (same IP + ports)  
✔ IPC namespace (interprocess communication)  
✔ localhost access to each other  
✔ Optional shared volumes

This makes Pods perfect for multi-container apps that must talk over localhost.

---

## 🤔 Why Pods?

Without pods:
- Each container gets its own IP address
- You must expose ports individually
- Containers cannot talk using `localhost`

With pods:
- Only the pod exposes ports
- All containers inside share network stack
- Containers communicate over `localhost` internally  
  Example: `nginx:80` can reach `redis:6379` instantly!

---

## 🏗️ Create a Pod

Create a pod named `mypod` and expose its port:
```bash
podman pod create --name mypod -p 8080:80
```

Flags:
- `--name` → friendly name
- `-p HOST:CONTAINER` → publish pod port

List pods:
```bash
podman pod ps
```

Inspect pod:
```bash
podman pod inspect mypod
```

---

## ➕ Add Containers to the Pod

Any container can join a pod using `--pod`:

```bash
podman run -d --pod mypod nginx
podman run -d --pod mypod redis
```

Verify:
```bash
podman ps
```

Check pod contents:
```bash
podman ps --pod
```

📌 Notice:
- Both containers have the **same IP**
- Both share the **pod’s mapped ports**
- External traffic only enters via `mypod`

---

## 🌐 Networking Inside Pod

Inside the pod:
- Containers can reach each other over `localhost`
- No publishing required internally

Example:
```bash
podman exec -it mypod-nginx bash
curl localhost:6379
```

To enter the Redis container:
```bash
podman exec -it mypod-redis sh
```

---

## 🧠 Namespace Sharing

Pods share:
- NET — network namespace
- IPC — message passing
- UTS — hostname
- cgroups (optional)
- PID (optional with `--share`)

---

## 🛑 Stop & Remove Pods

Stop all containers in pod:
```bash
podman pod stop mypod
```

Remove:
```bash
podman pod rm mypod
```

Force remove:
```bash
podman pod rm -f mypod
```

---

## 🪁 Pod With Custom Options

Share **PID namespace**:
```bash
podman pod create --name mypod --share pid
```

Assign labels:
```bash
podman pod create --label env=dev
```

Add volumes:
```bash
podman run -d --pod mypod -v data:/data redis
```

---

## 💡 Pod Lifecycle Summary

| Action | Command |
|--------|---------|
| Create pod | `podman pod create` |
| Add container | `podman run --pod` |
| List pods | `podman pod ps` |
| Inspect pod | `podman pod inspect` |
| Stop pod | `podman pod stop` |
| Remove pod | `podman pod rm` |

---

## 🧩 Architecture Diagram

```
         +----------------------------------+
         |             Pod: mypod           |
         |    Shared network : localhost    |
         |    Exposed port    : 8080        |
         |                                  |
    +------------------+    +------------------+
    | Container nginx  |    |  Container redis |
    | listens at :80   |    | listens at :6379 |
    +------------------+    +------------------+
         ^     LOCALHOST COMMUNICATION     ^
         +----------------------------------+
```

---

## 🎉 You Now Understand Pods!

✔ How to create & manage pods  
✔ How containers share network & IPC  
✔ How to exec and debug inside pod containers  
✔ How to remove pods safely  
✔ How pods mirror **Kubernetes Pod behavior**

➡ Next section: **[Podman Compose](compose.md)** to run many containers via YAML!
