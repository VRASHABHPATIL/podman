# 🧾 Cheat Sheet

### Containers
```
podman run -d nginx
podman ps -a
```

### Images
```
podman build -t app .
podman images
```

### Pods
```
podman pod ps
podman generate kube
```

### Cleanup
```
podman system prune -a -f
```
