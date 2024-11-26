#======================#
#         Docker       #
#======================#

# Local images - using local computer's architecture
# i.e. linux/amd64 for Windows / Linux / Apple with Intel chip
#      linux/arm64 for Apple with Apple Silicon (M1 / M2 chip)

# Cloud images - using architecture compatible with cloud, i.e. linux/amd64

# Define variables
GCR_MULTI_REGION = europe-west1-docker.pkg.dev
PROJECT_ID = le-wagon-data-science-376310
REPO_NAME = potluck-repo
DOCKER_IMAGE_NAME = potluck-img-2

# docker_build tags both latest for the most recent build, and prod for a stable release

docker_build:
	docker build \
		--platform linux/amd64 \
		-t $(GCR_MULTI_REGION)/$(PROJECT_ID)/$(REPO_NAME)/$(DOCKER_IMAGE_NAME):latest \
		-t $(GCR_MULTI_REGION)/$(PROJECT_ID)/$(REPO_NAME)/$(DOCKER_IMAGE_NAME):v2 \
		-t $(GCR_MULTI_REGION)/$(PROJECT_ID)/$(REPO_NAME)/$(DOCKER_IMAGE_NAME):prod .


# when docker_run is executed, a link will appear to do a test run locally.

docker_run:
	docker run \
		--platform linux/amd64 \
		-e PORT=8080 -p 8080:8080 \
		$(GCR_MULTI_REGION)/$(PROJECT_ID)/$(DOCKER_IMAGE_NAME):prod \
		streamlit run app.py --server.port 8080


docker_run_interactively:
	docker run -it \
		--platform linux/amd64 \
		-e PORT=8080 -p $(DOCKER_LOCAL_PORT):8080 \
		$(GCR_MULTI_REGION)/$(PROJECT_ID)/$(DOCKER_IMAGE_NAME):prod \
		bash

# Push and deploy to cloud

docker_push:
	docker push $(GCR_MULTI_REGION)/$(PROJECT_ID)/$(REPO_NAME)/$(DOCKER_IMAGE_NAME):v2


docker_deploy:
	gcloud run deploy \
		--project $(PROJECT_ID) \
		--image $(GCR_MULTI_REGION)/$(PROJECT_ID)/$(REPO_NAME)/$(DOCKER_IMAGE_NAME):v2 \
		--platform managed \
		--memory 4Gi \
		--min-instances 1 \
		--region europe-west1 \
		--allow-unauthenticated

# Verify existing images

docker_list:
	docker images

# Clean up local Docker images

docker_clean:
	docker system prune -f
