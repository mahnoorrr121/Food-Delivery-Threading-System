
import threading
import time

# Create an Event object
kitchen_ready = threading.Event()


def prepare_order(order_id):

    print(f"Worker {order_id} is waiting for the kitchen to open...")

    # Wait until the manager signals that kitchen is ready
    kitchen_ready.wait()

    print(f"Worker {order_id} started preparing the order")

    time.sleep(2)

    print(f"Worker {order_id} completed the order!")


def manager():

    print("\nManager is preparing the kitchen...")

    time.sleep(3)

    print("\nManager: Kitchen is READY!")

    # Send signal to all waiting workers
    kitchen_ready.set()


def main():

    print("FOOD DELIVERY SYSTEM - EVENT")

    workers = []

    # Start three kitchen workers
    for order_id in range(101, 104):

        worker = threading.Thread(
            target=prepare_order,
            args=(order_id,)
        )

        workers.append(worker)
        worker.start()

    # Start manager
    manager_thread = threading.Thread(target=manager)
    manager_thread.start()

    # Wait for workers and manager
    for worker in workers:
        worker.join()

    manager_thread.join()

    print("\nAll orders completed!")
    print("Kitchen operations completed.")


if __name__ == "__main__":
    main()
