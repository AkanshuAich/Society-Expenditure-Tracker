FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /SOCIETY-EXPENDITURE-TRACKER

COPY requirements.txt /SOCIETY-EXPENDITURE-TRACKER/

RUN pip install -r requirements.txt

COPY . /SOCIETY-EXPENDITURE-TRACKER/

CMD ["python" , "society_expenditure/manage.py" , "runserver" , "0.0.0.0:8000"]