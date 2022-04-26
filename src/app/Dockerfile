FROM python:3.7
 
WORKDIR /ml/app

COPY . .
RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port", "1234"]