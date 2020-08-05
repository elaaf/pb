# Test for basic progress bar working

# Add pb module directory to enable import
import sys
sys.path.append("..")

# Imports
import time

# Local Import
# NOTE: Maybe a better approach ?
from pb.pb.pb  import pb



MAX = 1000
MIN = 0
STEP = 1
array = range(MIN, MAX, STEP)


print("Executing loop with pb")


PAUSE_TIME = 0.005
info = "__test_info__"

for x in pb(array, info):
    time.sleep(PAUSE_TIME)
    pass
