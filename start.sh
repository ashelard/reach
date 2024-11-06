#!/bin/bash

set -e
scrapyd

cd /app/wb_spider
scrapyd-deploy

python3 manage.py runserver 0.0.0.0:80