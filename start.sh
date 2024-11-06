#!/bin/bash

set -e
scrapyd &

cd /app/wb_spider
scrapyd-deploy

python3 manage.py runserver 0.0.0.0:80
echo "start runserver end" >> logs/info-2024-11-06.log
