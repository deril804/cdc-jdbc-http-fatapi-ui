FROM python:latest

RUN pip install \
    psycopg2-binary \
    psycopg2 \
    faker 


WORKDIR /opt/datagen

COPY ../../datagen /opt/datagen

CMD [ "python" "./gen_user_payment_data.py"]