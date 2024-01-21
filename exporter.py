from prometheus_client import start_http_server, Gauge, Info
from mcrcon import MCRcon
import time
import os
import re

players_num = Gauge("players_num", "login players count")
rcon_failure_count = Gauge(
    "rcon_failure_count", "failure of execute to command by rcon"
)
server_info = Info("server_info", "server infomartion")


def update_palworld_stats(mcr):
    for _ in range(3):
        try:
            response = mcr.command("ShowPlayers")
            players_num.set(response.count("\n") - 1)
            break
        except:
            rcon_failure_count.inc()
            mcr.connect()


if __name__ == "__main__":
    rcon_address = os.environ.get("RCON_ADDRESS", "127.0.0.1")
    rcon_port = int(os.environ.get("RCON_PORT", "25575"))
    rcon_password = os.environ["RCON_PASSWORD"]

    time_window = int(os.environ.get("TIME_WINDOW", "10"))

    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    with MCRcon(rcon_address, rcon_password, rcon_port) as mcr:
        for _ in range(3):
            try:
                response = mcr.command("Info")
                server_name = re.sub("^.*?\[.*?\]\s", "", response)
                server_info.info(
                    {
                        "server_name": server_name,
                    }
                )
                break
            except:
                rcon_failure_count.inc()
                mcr.connect()

        while True:
            update_palworld_stats(mcr)
            time.sleep(time_window)
