# Imports
import time
from tqdm import tqdm

# Add one level up path to sys
# To enable pb local import
#import sys
#sys.path.append("..")


# Local Import
# NOTE: Maybe a better approach ?
#from pb.pb.pb  import pb



MAX = 1000
MIN = 0
STEP = 1
array = range(MIN, MAX, STEP)


print("Executing loop with pb")


PAUSE_TIME = 0.005
info = "__test_info__"

for x in tqdm(array, info):
    time.sleep(PAUSE_TIME)
    pass
