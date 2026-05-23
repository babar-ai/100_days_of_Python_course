Basic Commands of Docker 







1\. To pull image from docker hub or registory.



&nbsp;	docker pull <image name>                   # This only downloads the image to your local system.





2\. To run docker image

&nbsp;	

&nbsp;	docker run                                              # This tells Docker to create and start a new container from a given image.

&nbsp;	

&nbsp;	doecker run -d                               # called 'Detached mode' If you remove -d, Docker runs in the foreground, showing Nginx

&nbsp;						   logs until you stop it.

&nbsp;	-p <HOST\_PORT>:<CONTAINER\_PORT>           # <Contaniner port i.e 80> → port inside the container which is mentioned in docker file 



&nbsp;	docker run -d -p <HOST\_PORT>:<CONTAINER\_PORT> --name mynginx      # This assigns a custom name to your container



&nbsp;	





3\. To veriy the Container image is running or not

&nbsp;	docker ps



4. to stop running specific docker container
    docker stop <image name>



5. to build docker image

    1. create docker file 
        # Step 1: Start from a base image
        FROM python:3.10-slim

        # Step 2: Set working directory inside container
        WORKDIR /app

        # Step 3: Copy your project files into the container
        COPY . .

        # Step 4: Install dependencies
        RUN pip install -r requirements.txt

        # Step 5: Set default command
        CMD ["python", "app.py"]


    2. Build the Docker Image

        docker build -t <image name> . (Means "use the current directory" (where your Dockerfile is))
        