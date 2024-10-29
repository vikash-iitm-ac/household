# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /app/data && chmod 777 /app/data

# Copy the application code
COPY . .

# Set environment variables to enable auto-reloading
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose port for the Flask app
EXPOSE 5000

# Start Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--reload"]

