FROM python

ENV PYTHONUNBUFFERED=1
WORKDIR /code


COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY starter.sh /usr/bin/
COPY . .
RUN chmod +x /usr/bin/starter.sh






