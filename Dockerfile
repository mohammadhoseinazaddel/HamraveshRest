
FROM python:3.10 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system web \
    && adduser --system --ingroup web web\
    && pip install --upgrade pip\\
    && pip install djangorestframework-simplejwt==4.4.0\
    && pip install PyJWT==1.7.1
USER root
# Install os-level dependencies (as root)
RUN apt-get update && apt-get install -y -q --no-install-recommends \
  # dependencies for building Python packages
  build-essential \
  # postgress client (psycopg2) dependencies
  libpq-dev \
  # cleaning up unused files to reduce the image size
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
  && apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
# Switch to the non-root user
USER web
# Create a directory for the source code and use it as base path
WORKDIR /home/web/code/
# Copy the python depencencies list for pip
COPY --chown=web:web ./requirements/base.txt requirements/base.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "manage.py", "runserver"]

EXPOSE 8000
