#!/bin/bash

set -e
scrapyd &

cd /app/wb_spider
scrapyd-deploy

cd /app
python3 manage.py start_task &
python3 manage.py runserver 0.0.0.0:80
