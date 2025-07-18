# Sticky Notes Django App with Docker

**Author:** Giulia Damascena
**Date:** June 2025

---

## 📋 Description

This is a Django-based **Sticky Notes** web application, containerized using **Docker**.
It allows users to create, view, and manage sticky notes through a clean web interface.

 Ideal for learning and practicing Docker-based deployment.
 Easily accessible via [http://localhost:8000](http://localhost:8000) once the container is running.

---

## ⚠️ Prerequisites

Ensure the following are installed:

- 🐳 [Docker](https://www.docker.com/products/docker-desktop)
- 🌐 Internet access (to pull the Docker image)

---

##  Docker Image

**Docker Hub Repository:**
🔗 [giuliadamascena/sticky_notes](https://hub.docker.com/r/giuliadamascena/sticky_notes)

---

##  Getting Started with Docker

### 1️⃣ Pull the Docker image

docker pull giuliadamascena/sticky_notes

2️⃣ Run the container

docker run -d -p 8000:8000 giuliadamascena/sticky_notes
Then visit:
👉 http://localhost:8000

3️⃣ (Optional) Run Migrations
If necessary, apply Django migrations manually:

docker ps              # Find your container ID
docker exec -it <container_id> python manage.py migrate
