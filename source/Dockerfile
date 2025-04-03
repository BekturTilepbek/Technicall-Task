FROM python:3.12
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY source/ /code/
ENV PYTHONUNBUFFERED=1
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tech_task.wsgi:application"]
