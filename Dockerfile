FROM python:3.10

SHELL ["/bin/sh", "-c"]

WORKDIR /opt/django_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

RUN groupadd -r web && \
    useradd -r -g web -d /opt/django_api -s /sbin/nologin -c "Docker image user" web


COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini


RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/django_api/static/ \
     && mkdir -p /opt/django_api/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt


COPY . .
#RUN chown -R web:web /opt/django_api/static
#RUN python manage.py collectstatic --noinput
#RUN python manage.py makemigrations
#RUN python manage.py migrate --fake sessions zero && \
#    python manage.py migrate

EXPOSE 8000


#ENTRYPOINT ["uwsgi", "--strict", "--ini", "./uwsgi/uwsgi.ini"]
