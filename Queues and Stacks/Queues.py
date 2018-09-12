import queue

q = queue.Queue()
print(q.empty())
q.put("bag1")
print(q.empty())
q.put("bag2")
q.put("bag3")
print(q.get())
print(q.get())
print(q.get())
print(q.empty())

q2 = queue.Queue(2)
print(q.empty())
q.put("bag1")
print(q.full())
q.put("bag2")
print(q.full())
