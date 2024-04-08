#!/usr/bin/env bash

set -e

TIMEOUT=${WAIT_FOR_STARTUP:-300}
REST_API_HOST=${REST_API_HOST:-http://127.0.0.1:8212}
python /usr/local/bin/wait_for_http.py $REST_API_HOST $TIMEOUT

python exporter.py

