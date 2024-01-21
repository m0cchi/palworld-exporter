# What?
Prometheus exporter for Palworld dedicated server.

Palworld: https://store.steampowered.com/app/1623730/Palworld/

# Run
```bash
docker run -it -p 8000:8000 -e RCON_ADDRESS=$GAME_SERVER -e RCON_PORT=$RCON_PORT -e RCON_PASSWORD=$RCON_PASSWORD mocchi/palworld-exporter:latest
```

# Read Metrics
```bash
curl http://127.0.0.1:8000
```
