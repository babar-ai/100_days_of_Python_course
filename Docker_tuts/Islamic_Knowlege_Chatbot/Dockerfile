
# use offical python image       # specifies the Python version (here, Python 3.9). slim → means it’s a lightweight version of the image.It removes unnecessary packages, tools, and docs

FROM python:3.9-slim


# Set working directory , here note that 'DIR/app'  tells Docker: “inside the container, treat /app as the default folder for everything (COPY, RUN, CMD, etc.)”.
WORKDIR /app


# Copy dependency file & install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5000


CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "8000"]

