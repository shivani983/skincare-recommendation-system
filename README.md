# skincare-recommendation-system
ML model to recommend skincare products based on different criteria

## workflow
-config.yaml
-entity
-config/configuration.py
-components
-pipeline
-main.py
-app.py
# how to run?

### steps:

clone the repository

```bash
https://github.com/shivani983/skincare-recommendation-system.git
```

### step 01- create a conda environment after opening the repository

```bash
conda create --name skincare-recommendation python=3.10 -y
```

```bash
conda activate skincare-env

```
### step 02- install the required packages
```bash
pip install -r requirements.txt
```
# run the model
```bash
streamlit run app.py
```



# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t entbappy/stapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 entbappy/stapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push entbappy/stapp:latest 
```

```bash
docker rmi entbappy/stapp:latest
```

```bash
docker pull entbappy/stapp
```









