#!/usr/bin/env bash

set -e

TIMEOUT=${WAIT_FOR_STARTUP:-300}
python /usr/local/bin/wait_for_http.py $REST_API_HOST $TIMEOUT

python exporter.py

