from prometheus_client import start_http_server, Gauge, Info
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth
import urllib.parse as urlparse
import time
import os
import re


players_num = Gauge("players_num", "login players count")
server_fps = Gauge("server_fps", "server fps")
serverframetime = Gauge("serverframetime", "server frame time (ms)")
server_info = Info("server_info", "server infomartion")

def update_palworld_stats(session, restapi_host, auth):
    r = session.request("GET", urlparse.urljoin(restapi_host, "/v1/api/metrics"), auth=auth)
    r.raise_for_status()

    stats = r.json()
    players_num.set(stats["currentplayernum"])
    server_fps.set(stats["serverfps"])
    serverframetime.set(stats["serverframetime"])


if __name__ == "__main__":
    restapi_host = os.environ.get("REST_API_HOST", "http://127.0.0.1:8212")
    admin_name = os.environ.get("PALWORLD_ADMIN", "admin")
    password = os.environ["PALWORLD_PASSWORD"]
    auth=HTTPBasicAuth(admin_name, password)
    time_window = int(os.environ.get("TIME_WINDOW", "10"))

    session = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=1,
                    status_forcelist=[
                        500,
                        502,
                        503,
                        504,
                    ])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))


    # Start up the server to expose the metrics.
    start_http_server(8000)

    r = session.request("GET", urlparse.urljoin(restapi_host, "/v1/api/info"), auth=auth)
    r.raise_for_status()

    server_name = r.json()['servername']
    server_info.info(
        {
            "server_name": server_name,
        }
    )

    while True:
        update_palworld_stats(session, restapi_host, auth)
        time.sleep(time_window)

