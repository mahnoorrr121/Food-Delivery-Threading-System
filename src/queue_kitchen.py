
import threading
import queue
import time

# Create a shared order queue
order_queue = queue.Queue()

# Add customer orders to the queue
orders = [
    "Order 101 - Burger",
    "Order 102 - Pizza",
    "Order 103 - Pasta",
    "Order 104 - Sandwich",
    "Order 105 - Fries",
    "Order 106 - Burger"
]


def kitchen_worker(worker_name):

    while True:

        # Get an order from the queue
        order = order_queue.get()

        # Stop worker when queue is empty and stop signal is received
        if order is None:
            order_queue.task_done()
            break

        print(f"{worker_name} is preparing {order}")

        time.sleep(2)

        print(f"{worker_name} completed {order}\n")

        # Mark this order as completed
        order_queue.task_done()


def main():

    print("FOOD DELIVERY SYSTEM - QUEUE\n")

    # Add all orders to the queue
    for order in orders:
        order_queue.put(order)

    # Create two kitchen workers
    workers = []

    for i in range(1, 3):

        worker = threading.Thread(
            target=kitchen_worker,
            args=(f"Kitchen Worker {i}",)
        )

        workers.append(worker)
        worker.start()

    # Wait until all customer orders are processed
    order_queue.join()

    # Send stop signals to workers
    for worker in workers:
        order_queue.put(None)

    # Wait for workers to stop
    order_queue.join()

    for worker in workers:
        worker.join()

    print("All customer orders have been processed!")
    print("Kitchen operations completed.")


if __name__ == "__main__":
    main()
