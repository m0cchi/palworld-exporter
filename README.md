# What?
Prometheus exporter for Palworld dedicated server.

Palworld: https://store.steampowered.com/app/1623730/Palworld/

# Run
```bash
REST_API_HOST=${REST_API_HOST:-http://127.0.0.1:8212}
docker run -it -p 8000:8000 -e REST_API_HOST=$REST_API_HOST -e PALWORLD_PASSWORD=$PALWORLD_PASSWORD mocchi/palworld-exporter:latest
```

# Read Metrics
```bash
curl http://127.0.0.1:8000
```

