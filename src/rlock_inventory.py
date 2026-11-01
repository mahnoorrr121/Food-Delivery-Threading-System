
import threading
import time

# Shared kitchen inventory
inventory = {
    "Burger Buns": 10,
    "Pizza Bases": 8
}

# Create a reentrant lock
inventory_lock = threading.RLock()


def check_inventory(item):

    # First lock acquisition
    with inventory_lock:

        print("Checking inventory...")

        # Nested function acquires the same lock again
        update_inventory(item)


def update_inventory(item):

    # Same thread can acquire RLock again
    with inventory_lock:

        print("Updating inventory...")

        inventory[item] -= 2

        time.sleep(1)

        print(f"{item} remaining: {inventory[item]}")


def kitchen_worker():

    print("Kitchen worker started")

    check_inventory("Burger Buns")

    print("Kitchen worker completed!")


def main():

    print("FOOD DELIVERY SYSTEM - RLOCK")
    print("Initial Inventory:", inventory, "\n")

    worker = threading.Thread(target=kitchen_worker)

    worker.start()
    worker.join()

    print("\nFinal Inventory:", inventory)


if __name__ == "__main__":
    main()
