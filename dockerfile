# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy and install requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory for the SQLite database
RUN mkdir -p /app/db

# Copy the database initialization script and execute it
COPY init_db.py /app/
RUN python init_db.py

# Copy the current directory contents into the container at /app/
COPY . /app/

# Set permissions for the database directory
RUN chmod -R 755 /app/db

# Expose the port the app runs on
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]

