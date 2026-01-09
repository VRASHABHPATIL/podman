# 🏗️ Building Images

## Containerfile
```
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python","app.py"]
```

### Build
```
podman build -t flaskapp -f Containerfile .
```
