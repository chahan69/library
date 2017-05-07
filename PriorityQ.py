import itertools
import heapq as hq

class PriorityQ(object):
    def __init__(self,lis):
        hq.heapify(lis)
        self.pq = lis                        # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'      # placeholder for a removed task
        self.counter = itertools.count()     # unique sequence count

    def put(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            rem(task)
        count = next(self.counter)
        entry = [priority, task]
        self.entry_finder[task] = entry
        hq.heappush(self.pq, entry)

    def rem(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, task = hq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')


if __name__ == '__main__':
    q=PriorityQ([])
    q.put("A",0.5)
    q.put("B",0.3)
    q.put("C",0.4)
    print(q.pq)
    print(q.entry_finder)
    print(q.counter)
    print(q.pop())
    q.rem("C")
    print(q.pop())