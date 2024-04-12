FROM debezium/connect:latest

USER kafka

RUN curl --create-dirs -LO --output-dir /tmp/connector https://github.com/aiven/s3-connector-for-apache-kafka/releases/download/v2.12.0/aiven-kafka-connect-s3-2.12.0.zip && \
    unzip -o /tmp/connector/aiven-kafka-connect-s3-2.12.0.zip -d /tmp/connector && \
    mv /tmp/connector/aiven-kafka-connect-s3-2.12.0 /kafka/connect/aiven-kafka-connect-s3 && \
    rm /tmp/connector/aiven-kafka-connect-s3-2.12.0.zip

RUN curl --create-dirs -LO --output-dir /tmp/connector https://github.com/Aiven-Open/jdbc-connector-for-apache-kafka/releases/download/v6.8.0/jdbc-connector-for-apache-kafka-6.8.0.zip && \
    unzip -o /tmp/connector/jdbc-connector-for-apache-kafka-6.8.0.zip -d /tmp/connector && \
    mv /tmp/connector/jdbc-connector-for-apache-kafka-6.8.0 /kafka/connect/jdbc-connector-for-apache-kafka && \
    rm /tmp/connector/jdbc-connector-for-apache-kafka-6.8.0.zip

RUN curl --create-dirs -LO --output-dir /tmp/connector https://github.com/Aiven-Open/http-connector-for-apache-kafka/releases/download/v0.7.0/http-connector-for-apache-kafka-0.7.0.zip && \
    unzip -o /tmp/connector/http-connector-for-apache-kafka-0.7.0.zip -d /tmp/connector && \
    mv /tmp/connector/http-connector-for-apache-kafka-0.7.0 /kafka/connect/http-connector-for-apache-kafka && \
    rm /tmp/connector/http-connector-for-apache-kafka-0.7.0.zip
