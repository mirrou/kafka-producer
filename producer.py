from kafka import KafkaProducer
import json
import time
import random

# Constants
KAFKA_TOPIC = "vitals-data"  # Kafka topic to send messages to
KAFKA_BROKER = "my-cluster-kafka-bootstrap.hl7-listener.svc:9092"  # Replace with your Kafka broker URL and port

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_vitals():
    """Generate random vitals data as a dictionary."""
    vitals_data = {
        "heart_rate": random.randint(60, 100),
        "blood_pressure": f"{random.randint(90, 140)}/{random.randint(60, 90)}",
        "temperature": round(random.uniform(97.0, 99.5), 1)
    }
    return vitals_data

def send_vitals():
    """Generate vitals data and send it to the Kafka topic."""
    while True:
        vitals_data = generate_vitals()  # Generate random vitals data
        producer.send(KAFKA_TOPIC, value=vitals_data)  # Send data to Kafka topic
        print(f"Sent data: {vitals_data}")
        time.sleep(5)  # Wait for 5 seconds before sending the next set of data

if __name__ == "__main__":
    send_vitals()
