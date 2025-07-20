#!/bin/bash

export GOOGLE_GENAI_USE_VERTEXAI="True"
export GOOGLE_CLOUD_PROJECT="{{cookiecutter.project_id}}"
export GOOGLE_CLOUD_LOCATION="{{cookiecutter.location}}"

export AGENT_PATH="./{{cookiecutter.agent_name}}" # Assuming capital_agent is in the current directory
# Set a name for your Cloud Run service (optional)
export SERVICE_NAME="{{cookiecutter.agent_name}}"

# Set an application name (optional)
export APP_NAME="{{cookiecutter.repo_name}}-app"    

uv run adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH
