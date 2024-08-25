FROM confluentinc/cp-kafka-connect:7.7.0

# Uncomment and use the following lines to install any required plugins
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.0.0

# Copy any necessary configuration files
COPY connect-distributed.properties /etc/kafka/connect-distributed.properties

EXPOSE 8083

CMD ["connect-distributed", "/etc/kafka/connect-distributed.properties"]
