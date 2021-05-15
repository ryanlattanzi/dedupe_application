#!/bin/sh

APP_NAME="${PWD##*/}"

docker build -t "$APP_NAME":latest .