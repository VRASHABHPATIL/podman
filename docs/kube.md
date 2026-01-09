# ☸️ Podman Kube

Export Podman pods to Kubernetes YAML.

### Generate YAML
```
podman generate kube mypod > pod.yaml
```

### Launch:
```
podman kube play pod.yaml
```

### Remove:
```
podman kube down pod.yaml
```
