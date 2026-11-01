# Food Delivery Order Processing System

## Project Description

This project demonstrates the use of Python multithreading concepts through a Food Delivery Order Processing System.

In a food delivery system, multiple customer orders need to be processed at the same time. Instead of processing each order one by one, threads are used to handle different tasks concurrently.

The project uses sample food order data stored in a CSV file and demonstrates different Python threading concepts.

## Dataset

The project uses a fictional dataset named `orders.csv`, containing 12 food orders.

The dataset includes:
- Order ID
- Customer Name
- Food Item
- Quantity
- Price
- Preparation Time

## Threading Concepts Implemented

| Concept | Python File | Purpose |
|---|---|---|
| Basic Threads | `thread_definition.py` | Processes multiple food orders using separate threads. |
| Custom Thread Class | `my_thread_class.py` | Creates kitchen workers using a class that inherits from `threading.Thread`. |
| Lock | `lock_inventory.py` | Protects shared kitchen inventory from simultaneous updates. |
| RLock | `rlock_inventory.py` | Allows the same thread to acquire a lock multiple times. |
| Semaphore | `semaphore_kitchen.py` | Limits the number of workers using kitchen stations at once. |
| Event | `event_kitchen.py` | Allows workers to wait until the manager gives a start signal. |
| Condition | `condition_kitchen.py` | Coordinates kitchen preparation and delivery using notifications. |
| Queue | `queue_kitchen.py` | Assigns food orders to available worker threads. |
| Barrier | `barrier_delivery.py` | Makes delivery riders wait until all riders have arrived before starting. |

## Project Structure

```text
Food-Delivery-Threading-System/
│
├── data/
│   └── orders.csv
│
├── src/
│   ├── thread_definition.py
│   ├── my_thread_class.py
│   ├── lock_inventory.py
│   ├── rlock_inventory.py
│   ├── semaphore_kitchen.py
│   ├── event_kitchen.py
│   ├── condition_kitchen.py
│   ├── queue_kitchen.py
│   └── barrier_delivery.py
│
└── README.md
```

## Requirements

- Python 3.x
- Visual Studio Code (recommended)
- No external Python libraries are required. The project uses Python standard libraries.

## How to Run the Project

Open the terminal in the project folder and run the following commands individually:

```bash
python src/thread_definition.py
python src/my_thread_class.py
python src/lock_inventory.py
python src/rlock_inventory.py
python src/semaphore_kitchen.py
python src/event_kitchen.py
python src/condition_kitchen.py
python src/queue_kitchen.py
python src/barrier_delivery.py
```

## Expected Outcome

Each Python file demonstrates a different threading concept in the food delivery scenario. The output shows how multiple workers, kitchen tasks, and delivery riders can be coordinated using Python threading techniques.

## GitHub Version Control

The project is maintained using Git and GitHub.

The following commands are used for version control:

```bash
git status
git add .
git commit -m "Describe your changes"
git push
git pull
```

Meaningful commit messages are used to describe the changes made to the project.