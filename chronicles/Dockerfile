# Use the official Python base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the Django application files into the container
COPY . /app/

# Install the required dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Install Gunicorn
RUN pip install gunicorn

# Expose the appropriate port for Gunicorn
EXPOSE 8000

# Command to run Gunicorn with your Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "eges.wsgi:application"]
