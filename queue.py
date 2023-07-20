class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def isEmpty(self):
        return len(self.queue) == 0

    def display(self):
        if not self.isEmpty():
            print("Queue:")
            for item in self.queue:
                print(item, end=" ")
            print()
        else:
            print("Queue is empty.")

# Example usage:
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    q.display()  # Output: Queue: 10 20 30 40

    q.dequeue()
    q.dequeue()

    q.display()  # Output: Queue: 30 40

    print("Is queue empty?", q.isEmpty())  # Output: Is queue empty? False

    q.enqueue(50)
    q.enqueue(60)

    q.display()  # Output: Queue: 30 40 50 60

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    q.display()  # Output: Queue is empty.
    print("Is queue empty?", q.isEmpty())  # Output: Is queue empty? True
