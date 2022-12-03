
FROM python:3.10 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
USER root

RUN addgroup --system web \
    && adduser --system --ingroup web web\
    && pip install --upgrade pip\\
    && pip install djangorestframework-simplejwt==4.4.0\
    && pip install PyJWT==1.7.1


RUN apt-get update && apt-get install -y -q --no-install-recommends \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin\
  && rm -rf /var/lib/apt/lists/*

WORKDIR /home/web/code/

COPY . ./etc/hamravesh

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "manage.py", "runserver"]

EXPOSE 8000
