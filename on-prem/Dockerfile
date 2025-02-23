# Use Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Run the script
CMD ["python", "sample_data_generation.py"]
