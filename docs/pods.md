# 🫙 Pods

Pods share **network + IPC + storage**.

### Create Pod
```
podman pod create --name mypod -p 8080:80
```

### Add Containers
```
podman run -d --pod mypod nginx
podman run -d --pod mypod redis
```

### Diagram
```
+------------------------+
| Pod: mypod             |
| Shared network: :8080  |
|  + nginx   + redis     |
+------------------------+
```
