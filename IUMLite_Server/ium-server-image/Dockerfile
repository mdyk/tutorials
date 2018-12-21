# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run views.py when the container launches

ENV FLASK_APP ium
ENV FLASK_ENV development

#RUN export FLASK_APP=ium
#RUN export FLASK_ENV=development
CMD pip install -e .



CMD ["flask", "run"]
