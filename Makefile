.PHONY: docker-image
docker-image: 
	sh bin/build-docker-image.sh

# make docker-image

.PHONY: run-app
run-app:
	sh bin/run-app.sh $(config)

# make run-app config='config.yml'