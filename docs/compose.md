# 🤝 Podman Compose

`podman-compose` = run multi-container apps.

### Example
```
version: "3.9"
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  redis:
    image: redis
```
Start:
```
podman-compose up -d
```
