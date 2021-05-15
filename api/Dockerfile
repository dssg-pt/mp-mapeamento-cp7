FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

COPY ./app app
COPY ./db db

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]