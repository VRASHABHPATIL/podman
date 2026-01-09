---
title: Podman Compose
nav_order: 4
---

# 🤝 Podman Compose  
Podman Compose allows you to start **multiple containers together** using **one YAML file**, instead of typing long `podman run` commands.

It behaves like Docker Compose, but talks to Podman instead of Docker.

---

## 🎯 Why Use Podman Compose?

Without compose, you start containers individually:
```
podman run nginx
podman run redis
podman run postgres
```

Problems:
- Hard to remember arguments  
- Cannot auto-start dependencies  
- No single command to manage all services

With **podman-compose**:
✔ define everything in YAML  
✔ version control your deployments  
✔ one command starts EVERYTHING  
✔ one command stops EVERYTHING  
✔ automatic networking between services

---

## 🧱 Install Podman Compose

```bash
pip install podman-compose
```

Check version:
```bash
podman-compose --version
```

---

## 📦 Example: Web + Redis

Create a file named:
```
podman-compose.yml
```

Paste:
```yaml
version: "3.9"
services:
  web:
    image: nginx
    ports:
      - "8080:80"

  redis:
    image: redis
```

---

## ▶️ Running Compose

Start all services in background:
```bash
podman-compose up -d
```

View running containers:
```bash
podman ps
```

---

## 🔗 Networking Behavior

Podman Compose:
- automatically creates a shared network
- assigns DNS names based on service name

Examples:
```
web can reach redis using hostname: redis
redis can reach web using hostname: web
```

No manual `--network` needed 🌐

---

## 🔍 Logs

Tail logs for all services:
```bash
podman-compose logs -f
```

Logs for one service:
```bash
podman-compose logs web
```

---

## 🧠 Exec Into Service

```bash
podman-compose exec web bash
```

If using Alpine:
```bash
podman-compose exec redis sh
```

---

## 🔁 Restart and Recreate

Restart services:
```bash
podman-compose restart
```

Recreate after editing YAML:
```bash
podman-compose up --build -d
```

---

## 🛑 Stop + Clean Up

Stop containers:
```bash
podman-compose down
```

Stop + remove volumes:
```bash
podman-compose down -v
```

---

## 📦 Adding Volumes (Database)

```yaml
services:
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: pass
    volumes:
      - dbdata:/var/lib/mysql

volumes:
  dbdata:
```

---

## 🌍 Add Environment Variables

```yaml
services:
  api:
    build: .
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_USER: root
```

Check inside container:
```
printenv DB_HOST
```

---

## 💡 Compose + Custom Image

```yaml
services:
  app:
    build:
      context: .
      dockerfile: Containerfile
    ports:
      - "5000:5000"
```

Podman will auto-build when running:
```bash
podman-compose up --build
```

---

## 🧩 Architecture Diagram

```
               +--------------------------+
               | Podman Network (auto)    |
               |   myproject_default      |
               |                          |
        +------+----------+       +-------+-------+
        |   web service   | <---> |    redis      |
        |  nginx:80       |       | redis:6379    |
        +-----------------+       +---------------+
               |
        published to HOST
               |
         localhost:8080
```

---

## 🚀 Key Concepts Summary

| Feature | Explanation |
|--------|-------------|
| One command deploy | `podman-compose up` |
| Shared network | Services communicate by name |
| Volumes | Persist data across restarts |
| Logs | `podman-compose logs` |
| Restart | `podman-compose restart` |
| Stop/remove | `podman-compose down` |

---

## 🎉 You Now Can:
✔ run multi-container apps  
✔ build images + databases + frontend  
✔ manage everything with **1 YAML + 1 command**

➡ Next: **[Podman Kube](kube.md)** — export Pods & Compose to Kubernetes YAML!
