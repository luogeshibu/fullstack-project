import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["192.168.88.88:9092"],
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8")
)

def send_task_event(event: dict):
    print("Preparing to send Kafka event:", event)

    future = producer.send("task-events", event)
    result = future.get(timeout=10)

    print("Kafka event sent successfully:", event)
    print("Kafka metadata:", result)