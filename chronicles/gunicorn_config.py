import multiprocessing

# Bind to 0.0.0.0:8000 so that Gunicorn can listen on all available network interfaces
bind = "0.0.0.0:8000"

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Use the "threads" worker type for better efficiency
worker_class = "gthread"

# Set the maximum number of simultaneous clients that a worker can handle
worker_connections = 1000

# Set the maximum number of requests a worker can handle before being restarted
max_requests = 1000

# Enable Gunicorn to daemonize and run in the background
daemon = True

# Set the path to the Gunicorn process ID file
pidfile = "/var/run/gunicorn.pid"

# Set the path to the Gunicorn access log file
accesslog = "/var/log/gunicorn/access.log"

# Set the path to the Gunicorn error log file
errorlog = "/var/log/gunicorn/error.log"
