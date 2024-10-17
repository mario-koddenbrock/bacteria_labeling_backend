# Base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 9090

# Run the ML backend
CMD ["python", "backend/app.py"]
