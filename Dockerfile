# Use an official, lightweight Python blueprint
FROM python:3.11-slim

# Keep Python clean by stopping it from writing extra scratch files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the operational command room inside our container
WORKDIR /app

# Install native system tools required to connect with our PostgreSQL database
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy our package list inside and install everything
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all our local backend project files into the container
COPY . /app/

# Open up port 8000 so we can access our backend API
EXPOSE 8000

# Tell Docker how to boot up our local backend testing server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]