FROM python:3.10

WORKDIR /code

# CREATE REQUIREMENTS FIlE
COPY Pipfile.lock /code/Pipfile.lock
RUN pip install pipenv
RUN pipenv requirements > /code/requirements.txt
RUN pip uninstall pipenv -y

# INSTALL DEPENDENCIES
RUN pip install --no-cache-dir -r /code/requirements.txt

# COPY SOURCE CODE
COPY ./app /code/app

# RUN API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]