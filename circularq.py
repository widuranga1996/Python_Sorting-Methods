class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full. Cannot enqueue.")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty. Cannot dequeue.")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return item

    def isEmpty(self):
        return self.front == -1

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()

# Example usage:
if __name__ == "__main__":
    ob = CircularQueue(5)

    ob.enqueue(14)
    ob.enqueue(22)
    ob.enqueue(13)
    ob.enqueue(-6)

    ob.display()  # Output: Circular Queue: 14 22 13 -6

    print("Deleted value = ",ob.dequeue())
    print("Deleted value = ",ob.dequeue())
    
    ob.display()  # Output: Circular Queue: 13 -6
    
    ob.enqueue(9)
    ob.enqueue(20)
    ob.enqueue(5)
    
    ob.display()  # Output: Circular Queue: 13 -6 9 20 5
