from numpy import random

# allocates the structure holding the pids, in this case just a simple array
def allocate_map():
  arr = []
  return arr

# generates a random pid, checks if its within range and if its already in use
# if not in use, allocates the pid; otherwise checks next possible integer(+1)
def allocate_pid():
  NEW_PID = random.randint(MIN_PID, MAX_PID)
  inserted=False
  print("Attempting to allocate a new process to ID %s..." %(NEW_PID))
  if(NEW_PID>=MIN_PID and NEW_PID<=MAX_PID):
    print("ID within range...")
    while inserted==False:
      if not PIDS_IN_USE.__contains__(NEW_PID):
        print("ID %s not in use..."%(NEW_PID))
        PIDS_IN_USE.append(NEW_PID)
        inserted=True
        print("Process established on PID %s."%(NEW_PID))
      else:
        print("A PROCESS IS ALREADY RUNNING ON ID %s... ATTEMPTING %s."
                %(NEW_PID, NEW_PID+1))
        NEW_PID+=1
  else:
    print("ERR: ID %s NOT WITHIN RANGE!" %(NEW_PID))

# checks if pid to release is in use. if it is, releases it
def release_pid(int_pid):
  print("Attempting to release ID %s..." %(int_pid))
  if(PIDS_IN_USE.__contains__(int_pid)):
    PIDS_IN_USE.remove(int_pid)
    print("ID %s released." %(int_pid))
  else:
    print("ERR: NO PROCESS RUNNING ON ID %s!" %(int_pid))

# sets allowed range (300, 5000)
MIN_PID = 300
MAX_PID = 5001

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# testing the functions:

# calls allocate_map():
PIDS_IN_USE = allocate_map()

print("PIDS_IN_USE before calling allocate_pid(): %s \n" %(PIDS_IN_USE))
# calls allocate_pid() 5 times:
print("Calling allocate_pid() 5 times:\n")
i=0
while i!=5:
  allocate_pid()
  print("----------------------------------")
  i+=1

# calls release_pid(1234):
# adding 1234 to the array just for the sake of testing release_pid() 
# since allocate_pid() is random 
print("\nPIDS_IN_USE after calling allocate_pid() 5 times: %s" %(PIDS_IN_USE))
print ("\nadding 1234 for testing...")
PIDS_IN_USE.append(1234)
print("\nPIDS_IN_USE before calling release_pid(1234): %s" %(PIDS_IN_USE))
release_pid(1234)
print("PIDS_IN_USE after calling release_pid(1234): %s" %(PIDS_IN_USE))
