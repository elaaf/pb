import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


import time
from pb import pb


array = range(0,1000,1)

print("Executing loop")
for x in pb(array):
    time.sleep(0.01)
    pass