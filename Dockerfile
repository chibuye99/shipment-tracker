# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app


# Install any needed packages specified in requirements.txt
COPY requirements.txt .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

#Create a non-root user and switch to that user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser    

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set production default
ENV FLASK_ENV=production

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# Start command
CMD ["python", "app.py"]
