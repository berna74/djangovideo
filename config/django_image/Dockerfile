FROM python:3.12-bookworm

RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential python3-dev libpq-dev graphviz-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN pip install --upgrade pip setuptools

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN mkdir /scripts
COPY runserver.sh /scripts
RUN chmod +x /scripts -R

CMD ["/scripts/runserver.sh"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]