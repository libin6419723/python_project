#!/data/test/python/venv/bin/python3

from classes.Time import Time

import time
from datetime import datetime


a = [ 'a', 'b', 'c'];

b = a.index('a');
print(b)
exit(0);

print(time.time())
t =time.localtime()
print(type(t))
time = Time()

print("hello")

dt = datetime.now();
print(dt)
print(type(dt))
