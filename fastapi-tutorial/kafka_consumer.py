import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "task-events",
    bootstrap_servers=["192.168.88.88:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="task-log-consumer",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Kafka consumer started...")

for message in consumer:
    print("Received task event:", message.value)