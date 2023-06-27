# Use python:3.10-alpine as base image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN apk add --no-cache python3 \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools  \
    && ln -s pip3 /usr/bin/pip \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && rm -r /root/.cache \
    && pip install -r requirements.txt

# Copy the application code
COPY . .

# Set the working directory for the frontend
WORKDIR /app/frontend

# Install Node.js and npm
RUN apk add --no-cache nodejs npm

# Install frontend dependencies
RUN npm ci

# Build the React application
RUN npm run build

# Go back to the root directory
WORKDIR /app

# Collect the Django static files
RUN python manage.py collectstatic --noinput

# Expose the port the application will run on
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
