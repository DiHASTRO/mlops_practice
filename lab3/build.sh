#!/bin/bash
COMMIT_HASH=$(git rev-parse --short HEAD)
docker build -t lab3_streamlit-app:$COMMIT_HASH -t lab3_streamlit-app:latest .

docker tag lab3_streamlit-app:$COMMIT_HASH dihastro/lab3_streamlit-app:$COMMIT_HASH
docker tag lab3_streamlit-app:latest dihastro/lab3_streamlit-app:latest

docker push dihastro/lab3_streamlit-app:$COMMIT_HASH
docker push dihastro/lab3_streamlit-app:latest
