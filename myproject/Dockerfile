# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# COPY /app
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the default Django port
EXPOSE 8000

# Default command: Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]