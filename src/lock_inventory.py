
import threading
import time

# Shared kitchen inventory
inventory = {
    "Burger Buns": 10,
    "Pizza Bases": 8,
    "Pasta Packs": 12
}

# Create a lock
inventory_lock = threading.Lock()


def update_inventory(item, quantity, worker_name):

    print(f"{worker_name} is waiting to update {item}")

    # Only one worker can access inventory at a time
    with inventory_lock:

        print(f"{worker_name} is updating inventory")

        current_stock = inventory[item]

        time.sleep(1)

        inventory[item] = current_stock - quantity

        print(f"{worker_name} used {quantity} {item}")
        print(f"Remaining {item}: {inventory[item]}\n")


def main():

    print("FOOD DELIVERY SYSTEM - INVENTORY LOCK")
    print("Initial Inventory:", inventory, "\n")

    worker1 = threading.Thread(
        target=update_inventory,
        args=("Burger Buns", 4, "Kitchen Worker 1")
    )

    worker2 = threading.Thread(
        target=update_inventory,
        args=("Burger Buns", 3, "Kitchen Worker 2")
    )

    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()

    print("Final Inventory:", inventory)
    print("Inventory updates completed!")


if __name__ == "__main__":
    main()
