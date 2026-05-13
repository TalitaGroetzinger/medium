# import the python image. 
# use the slim variant to minimize container size.
# if the image does not exist locally, docker will pull it from the Docker hub automatically  
FROM python:3.14-slim

# set working directory to copy our code. 
WORKDIR /backend

#copy requirements file to working directory
COPY ./requirements.txt /backend/requirements.txt

# upgrade pip and install dependencies, avoiding cache to reduce image size.
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

#copy project files to working directory
COPY ./app /backend/app

# run my fastapi backend server using the default port 80.
CMD ["fastapi", "run", "app/main.py", "--port", "80", "--reload"]