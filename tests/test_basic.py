import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


import time
from pb import pb


array = range(0,100,1)

print("Executing loop")
index = 0
for x in pb(array, desc="Epoch"):
    index += 1
    time.sleep(0.1)
    pass