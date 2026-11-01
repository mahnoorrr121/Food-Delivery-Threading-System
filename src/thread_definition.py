
import csv
import threading
import time
from pathlib import Path

# Read customer orders from our CSV dataset
file_path = Path(__file__).resolve().parent.parent / "data" / "orders.csv"

orders = []

with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(line for line in file if line.strip())

    for order in reader:
        orders.append(order)


# Function executed by each thread
def process_order(order):

    order_id = order["order_id"]
    customer = order["customer"]
    item = order["item"]
    prep_time = int(order["prep_time"])

    print(f"{threading.current_thread().name}: "
          f"Preparing order {order_id} for {customer}")

    # Simulate food preparation time
    time.sleep(prep_time)

    total = int(order["quantity"]) * int(order["price"])

    print(f"{threading.current_thread().name}: "
          f"Order {order_id} completed! "
          f"Item: {item}, Total: Rs. {total}")


def main():

    threads = []

    print("FOOD DELIVERY ORDER PROCESSING SYSTEM")
    print("Starting kitchen workers...\n")

    # Create one thread for each customer order
    for order in orders:

        thread = threading.Thread(
            target=process_order,
            args=(order,),
            name=f"Worker-{order['order_id']}"
        )

        threads.append(thread)

        # Start the thread
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("\nAll customer orders have been processed!")
    print("Kitchen operations completed.")


if __name__ == "__main__":
    main()
