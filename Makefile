#======================#
#         Docker       #
#======================#

# Local images - using local computer's architecture
# i.e. linux/amd64 for Windows / Linux / Apple with Intel chip
#      linux/arm64 for Apple with Apple Silicon (M1 / M2 chip)



# Cloud images - using architecture compatible with cloud, i.e. linux/amd64

docker_build:
	docker build \
		--platform linux/amd64 \
		-t $(GCR_MULTI_REGION)/$(PROJECT_ID)/$(DOCKER_IMAGE_NAME):prod .

# when docker_run is executed, a link will appear to do a test run locally. When opening this link, change the port no. to 8080 manually
docker_run:
	docker run \
		--platform linux/amd64 \
		-e PORT=8000 -p $(DOCKER_LOCAL_PORT):8000 \
		$(GCR_MULTI_REGION)/$(PROJECT_ID)/$(DOCKER_IMAGE_NAME):prod

docker_run_interactively:
	docker run -it \
		--platform linux/amd64 \
		-e PORT=8000 -p $(DOCKER_LOCAL_PORT):8000 \
		$(GCR_MULTI_REGION)/$(PROJECT_ID)/$(DOCKER_IMAGE_NAME):prod \
		bash

# Push and deploy to cloud

docker_push:
	docker push $(GCR_MULTI_REGION)/$(PROJECT_ID)/$(DOCKER_IMAGE_NAME):prod

docker_deploy:
	gcloud run deploy \
		--project $(PROJECT_ID) \
		--image $(GCR_MULTI_REGION)/$(PROJECT_ID)/$(DOCKER_IMAGE_NAME):prod \
		--platform managed \
		--memory 4Gi \
		--min-instances 1 \
		--region europe-west1
