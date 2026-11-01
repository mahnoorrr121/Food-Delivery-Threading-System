
import threading
import time
import random

# All 3 riders must reach the pickup point
delivery_barrier = threading.Barrier(3)


def delivery_rider(rider_name):

    arrival_time = random.randint(1, 4)

    print(f"{rider_name} is travelling to the pickup point...")

    time.sleep(arrival_time)

    print(f"{rider_name} has arrived and is waiting.")

    # Wait until all 3 riders arrive
    delivery_barrier.wait()

    print(f"{rider_name} is now starting the delivery!")


def main():

    print("FOOD DELIVERY SYSTEM - BARRIER\n")

    riders = []

    for i in range(1, 4):

        rider = threading.Thread(
            target=delivery_rider,
            args=(f"Delivery Rider {i}",)
        )

        riders.append(rider)
        rider.start()

    for rider in riders:
        rider.join()

    print("\nAll riders have started their deliveries!")


if __name__ == "__main__":
    main()
