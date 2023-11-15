# pull official base image
FROM python:3.9.6-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings

# Instala los paquetes necesarios, incluido postgresql
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

# Copia los archivos de tu aplicación al directorio de trabajo
COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
