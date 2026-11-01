
import threading
import time

# Create a Condition object
order_condition = threading.Condition()

# Shared order status
order_ready = False


def kitchen_worker():

    global order_ready

    print("Kitchen worker: Preparing the food...")

    time.sleep(3)

    with order_condition:

        order_ready = True

        print("Kitchen worker: Order is ready!")

        # Notify the waiting delivery worker
        order_condition.notify()


def delivery_worker():

    global order_ready

    print("Delivery worker: Waiting for the order...")

    with order_condition:

        # Wait until the order is ready
        while not order_ready:
            order_condition.wait()

        print("Delivery worker: Order received!")
        print("Delivery worker: Going for delivery...")


def main():

    print("FOOD DELIVERY SYSTEM - CONDITION\n")

    kitchen = threading.Thread(target=kitchen_worker)
    delivery = threading.Thread(target=delivery_worker)

    # Start delivery worker first so it can wait
    delivery.start()

    time.sleep(1)

    # Start kitchen worker
    kitchen.start()

    delivery.join()
    kitchen.join()

    print("\nDelivery process completed!")


if __name__ == "__main__":
    main()
