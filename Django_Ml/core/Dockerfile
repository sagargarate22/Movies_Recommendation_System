# Use slim version of Python
FROM python:3.11-slim

# Disable .pyc and enable real-time logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Install Python dependencies
COPY ../requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (including model)
COPY core/ .

# Expose the Django dev server port
EXPOSE 8000

# Run Django dev server (use gunicorn in production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
