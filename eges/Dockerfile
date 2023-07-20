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

# Run migrations
RUN python manage.py makemigrations myapp
RUN python manage.py migrate

# Install Gunicorn
RUN pip install gunicorn

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the appropriate port
EXPOSE 8000

# Command to run Gunicorn with your Django application
CMD ["gunicorn", "eges.wsgi:application", "--bind", "0.0.0.0:8000"]
