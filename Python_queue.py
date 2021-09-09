#Creating queue in Python
from collections import deque

queue = deque()

queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
queue.append('e')
queue.append('f')

print (queue)

var1  = queue.popleft()
var2  = queue.popleft()
var3  = queue.popleft()

print (var1)
print (var2)
print (var3)

print (queue)
