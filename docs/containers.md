# 🐳 Containers

## 👉 Pull Images
```
podman pull nginx:latest
```

## 👉 Run Container
```
podman run -d -p 8080:80 nginx
```

## 👉 Inspect / Logs
```
podman inspect nginx
podman logs <id>
```

## Architecture
```
+-----------+
| nginx     |
| container |
+-----------+
   | port 80
   v
localhost:8080
```
