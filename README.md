# Teleport
Scalable Tracking Number Generator API - a RESTful API that generates unique tracking numbers for parcels.

# Setup steps
- To create virtualenv `python -m venv venv`
- Activate env `source venv/bin/activate`
- Install `pip install -r requirements.txt`
- Migrations `python manage.py makemigations`
- Migrate `python manage.py migrate`
- Run `python manage.py runserver`


# Celery
celery -A configs.worker worker -l INFO -P gevent -c 1000


# App
- Create tracking number POST http://127.0.0.1:8000/next-tracking-number/

# API Docs Swagger
http://127.0.0.1:8000/docs/


# Load balancing
- Install nginx
- Create nginx site move file using `mv` `nginx/default.conf` to `/etc/nginx/sites-available/default.conf`
- `sudo ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled`
- `sudo nginx -t`
- `sudo systemctl restart nginx`
