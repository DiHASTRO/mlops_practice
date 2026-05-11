#!/bin/bash
COMMIT_HASH=$(git rev-parse --short HEAD)
docker build -t lab3_streamlit-app:$COMMIT_HASH -t lab3_streamlit-app:latest .
