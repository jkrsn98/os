from numpy import random

def create_random_array(MIN_PID, MAX_PID):
  arr = []

  i = MIN_PID
  while i<=MAX_PID:
    arr.append(i)
    i = i+random.randint(1,3)

  return arr

MIN_PID = 300
MAX_PID = 500

PID_ARRAY = create_random_array(MIN_PID, MAX_PID)
print(PID_ARRAY)

NEW_PID = random.randint(300,501)
inserted=False
print("Attempting to allocate a new process to ID %s..." %(NEW_PID))  
if(NEW_PID>=MIN_PID and NEW_PID<=MAX_PID):
  print("ID within range...")
  while inserted==False:
    if not PID_ARRAY.__contains__(NEW_PID):
      print("ID %s not in use..."%(NEW_PID))
      PID_ARRAY.append(NEW_PID)
      inserted=True
      print("Process established on PID %s."%(NEW_PID))
    else:
      print("ERR: A PROCESS IS ALREADY RUNNING ON ID %s! ATTEMPTING %s." %(NEW_PID, NEW_PID+1))
      NEW_PID+=1
else:
  print("ERR: ID %s NOT WITHIN RANGE!" %(NEW_PID))
