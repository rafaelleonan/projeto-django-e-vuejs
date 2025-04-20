FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install django pillow

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]