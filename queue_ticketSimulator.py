import time
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []

        for i in range(1, 100):
            pq.enqueue("osoba nr " + str(i))

        now = time.time()
        t_end = now + till_show
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print("Obsluzono: " + str(person))
            tix_sold.append(person)

        return tix_sold

# Example use:
queue = Queue()
sold = queue.simulate_line(20, 4)
print(sold)
