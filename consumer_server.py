from  confluent_kafka  import Consumer
    
    
c = Consumer({"bootstrap.servers": "localhost:9092", "group.id": "0"})
c.subscribe(["com.udacity.police.calls"])
while True:
    message = c.poll(1.0)
    if message is None:
        print("no message received by consumer")
    elif message.error() is not None:
        print(f"error from consumer {message.error()}")
    else:
        print(f"consumed message {message.key()}: {message.value()}")
    
