# app --> os | python (a particular version) | venv | dependencies | compatible 
# docker helps --> build , package , deploy || it solves the problem of "it works on my machine" by creating a consistent environment across
# development , testing and production || docker containers encapsulate everything an app needs like code , libraries and dependencies
# ensuring it runs reliably on any system 

# Benefits of Docker 1. Portability Docker containers can run consistently across different environments. 
# Example, a container running on your laptop will work the same on a cloud server. 
# 2. Isolation Each Docker container is isolated from others, which means apps won't interfere with one another.
#  This is useful when running multiple services or apps on the same machine without worrying about compatibility issues. 
# 3. Scalability Docker makes scaling apps easier. For example, if a web service is getting high traffic, you can quickly spin up 
# more containers to handle the load. And when the traffic decreases, you can remove containers to save resources.


# Docker containers share the host operating system and use fewer resources, making them lightweight. 
# Starting a container takes seconds. Example, if you need to run 10 microservices, each can run in its own container, 
# using less memory and starting quickly. 


# Virtual machines run a full OS for each instant, making them heavy and slower to start. 
# They consume more resources because they need to virtualize hardware, not just the app.
#  Example, running the same 10 microservices in VMs will require significantly more memory and CPU because each VM has 
# its own operating system.

# dockerfile is used for creating packages 

# Dockerfile. It is a text file with instructions on how to build a Docker image. 
# It's a blueprint for the image, specifying the environment, app, and dependencies. Key components.
# From. Specifies the base image. Copy or add. Adds files from your host system into the image. 
# Run. Executes commands in the image, such as installing software. 
# CMD or Entry Point. Defines the command that runs when the container starts. 
# Expose. Specifies the port the container will listen on.


# docker desktop --> just like we install git so we can connect to github
# dockerhub --> remote repo where we push images (ex github in code versioning sense)

# Container → A running app in its own isolated box.
# 👉 Example: A Flask app running in one container, MySQL running in another.

# Image → A blueprint (recipe) to create containers.
# 👉 Example: python:3.8-slim is an image; your Flask app built on it becomes a new image.

# Volume → A storage space outside the container, so data is not lost when container stops.
# 👉 Example: MySQL database files saved in a volume so they survive container restarts.

# Build → The process of turning a Dockerfile into an image.
# 👉 Example: docker build -t myapp . builds your Flask app image

# Scout → Docker’s tool for checking vulnerabilities in images.
# 👉 Example: docker scout cves myapp tells if your app has security issues

# Extensions → Extra plugins you can add to Docker Desktop for specific tasks.
# 👉 Example: Kubernetes extension for managing clusters, or VSCode extension for coding inside containers.

# Docker → The whole tool/platform that manages images, containers, volumes, and networks.
# 👉 Think of it as the engine running the whole system.

# docker build codes
# docker build -t mlops-docker-demo .
# docker run -p 5000:5000 mlops-docker-demo
# docker tag mlops-docker-demo username/mlops-docker-demo:latest
# docker push username/mlops-docker-demo:latest
# docker pull username/mlops-docker-demo:latest
