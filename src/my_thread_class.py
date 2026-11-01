
import csv
import threading
import time
from pathlib import Path


# Read customer orders from CSV dataset
file_path = Path(__file__).resolve().parent.parent / "data" / "orders.csv"

orders = []

with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(line for line in file if line.strip())

    for order in reader:
        orders.append(order)


# Creating our own thread class
class MyThreadClass(threading.Thread):

    def __init__(self, order):
        super().__init__()
        self.order = order

    # This method runs when start() is called
    def run(self):

        order_id = self.order["order_id"]
        customer = self.order["customer"]
        item = self.order["item"]
        prep_time = int(self.order["prep_time"])

        print(f"{self.name}: Preparing order {order_id} for {customer}")

        time.sleep(prep_time)

        total = int(self.order["quantity"]) * int(self.order["price"])

        print(f"{self.name}: Order {order_id} completed!")
        print(f"Item: {item}, Total: Rs. {total}\n")


def main():

    threads = []

    print("FOOD DELIVERY SYSTEM - MY THREAD CLASS")
    print("Starting kitchen workers...\n")

    for order in orders:

        worker = MyThreadClass(order)
        worker.name = f"Kitchen-Worker-{order['order_id']}"

        threads.append(worker)
        worker.start()

    for worker in threads:
        worker.join()

    print("All orders have been processed!")
    print("Kitchen operations completed.")


if __name__ == "__main__":
    main()
