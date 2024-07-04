FROM python:3
WORKDIR /myapp

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install cryptography

COPY . .

CMD [ "python3","app.py" ]



# # Use the official Python image from Docker Hub
# FROM python:3

# # Set the working directory inside the container
# WORKDIR /myapp

# # Copy the requirements.txt file and install dependencies
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# RUN pip install cryptography

# # Copy the rest of the application code
# COPY . .

# # Install MySQL client in the Docker image
# # RUN docker pull mysql 

# # Set up MySQL environment variables
# ENV MYSQL_ROOT_PASSWORD=root
# ENV MYSQL_DATABASE=database1

# # Command to run when the container starts
# CMD ["sh", "-c", "python3 app.py && sleep infinity"]
