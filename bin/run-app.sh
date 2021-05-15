#!/bin/sh

APP_NAME="${PWD##*/}"
TEMP=' ' read -r -a ARGS <<< "$@"
CONFIG=${ARGS[0]}

echo 'Starting Container:' ${APP_NAME}
docker run \
    -v $(pwd)/outputs:/tmp/outputs \
	-v $(pwd)/input_data:/tmp/inputs \
	-v $(pwd)/config:/tmp/config \
	--name ${APP_NAME} \
	${APP_NAME}:latest \
	-c "${CONFIG}"

docker stop ${APP_NAME}
docker rm ${APP_NAME}
echo 'Stopped and Removed Container:' ${APP_NAME}