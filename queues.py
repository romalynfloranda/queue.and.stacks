# for queue data type

from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

#interactive
# from queues import Queue

# fifo = Queue()
# fifo.enqueue("1st")
# fifo.enqueue("2nd")
# fifo.enqueue("3rd")

# fifo.dequeue()
# fifo.dequeue()
# fifo.dequeue()

from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# interactive
# from queues import Queue

# fifo = Queue("1st", "2nd", "3rd")
# len(fifo)


# for element in fifo:
#     print(element)

# len(fifo)


#for building stack data type

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

#interactive
# from queues import Stack

# lifo = Stack("1st","2nd", "3rd")
# for element in lifo:
#     print (element)


# lifo = []
# lifo.append("1st")
# lifo.append("2nd")
# lifo.append("3rd")
# lifo.pop()
# lifo.pop()
# lifo.pop()

#for representing priority queques with a heap

#interactive
# from heapq import heappush

# fruits = []
# heappush(fruits,"orange")
# heappush(fruits,"apple")
# heappush(fruits,"banana")
# fruits

# from heapq import heappop
# heappop(fruits)
# fruits

# person1 = ("John", "Brown", 42)
# person2 = ("John", "Doe", 42)
# person3 = ("John", "Doe", 24)

# person1 < person2
# person2 < person3

#for building a priority queue data type

from collections import deque
from heapq import heappop, heappush

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)

#interactive
# from queues import PriorityQueue

# CRITICAL = 3
# IMPORTANT = 2
# NEUTRAL = 1

# messages = PriorityQueue()
# messages.enqueue_with_priority(IMPORTANT,"Windshield wipers turned on")
# messages.enqueue_with_priority(NEUTRAL,"Radio station tuned in")
# messages.enqueue_with_priority(CRITICAL,"Brake pedal depressed")
# messages.enqueue_with_priority(IMPORTANT,"Hazard lights turned on")

# messages.dequeue()

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, value))

    def dequeue(self):
        return heappop(self._elements)[1]

#interactive
# messages.dequeue()
# messages.dequeue()
# messages.dequeue()
# messages.dequeue()

#for handling corner cases in your priority queue
#interactive
# from dataclasses import dataclass

# @dataclass
# class Message:
#     event: str

# wipers = Message("Windshield wipers turned on")
# hazard_lights = Message("Hazard lights turned on")

# wipers < hazard_lights

# messages = PriorityQueue()
# messages.enqueue_with_priority(CRITICAL, wipers)
# messages.enqueue_with_priority(IMPORTANT, hazard_lights)

# messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))


from collections import deque
from heapq import heappop, heappush
from itertools import count

class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]

#for refactoring the code using a mixin class

class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(IterableMixin):
    ...

class Stack(Queue):
    ...

class PriorityQueue(IterableMixin):
    ...