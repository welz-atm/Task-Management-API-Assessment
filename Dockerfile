FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY ./requirements.txt /code/
ENV DJANGO_SETTINGS_MODULE=taskManagement.settings
RUN apt-get update && \
    apt-get install -y gcc && \
    pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && daphne -b 0.0.0.0 -p 8000 taskManagement.asgi:application"]
