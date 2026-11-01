
import threading
import time

# Only 2 workers can use cooking stations at once
kitchen_semaphore = threading.Semaphore(2)


def prepare_order(order_id):

    print(f"Worker for Order {order_id} is waiting for a cooking station")

    with kitchen_semaphore:

        print(f"Worker for Order {order_id} got a cooking station")

        time.sleep(3)

        print(f"Order {order_id} is ready!")

    print(f"Cooking station released by Order {order_id}\n")


def main():

    print("FOOD DELIVERY SYSTEM - SEMAPHORE")
    print("Available cooking stations: 2\n")

    threads = []

    # Create 5 kitchen workers
    for order_id in range(101, 106):

        worker = threading.Thread(
            target=prepare_order,
            args=(order_id,)
        )

        threads.append(worker)
        worker.start()

    for worker in threads:
        worker.join()

    print("All orders have been prepared!")
    print("Kitchen operations completed.")


if __name__ == "__main__":
    main()
