# Use official Python 3.11 image (slim = lightweight)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (for better caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy all source code
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Command to run your application
CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "8000"]