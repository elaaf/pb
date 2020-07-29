#Test for basic progress bar working

import sys
sys.path.append("..")

import time
from pb.pb.pb  import pb


array = range(0,100,1)

print("Executing loop")
index = 0
for x in pb(array, desc="Epoch"):
    index += 1
    time.sleep(0.1)
    pass
