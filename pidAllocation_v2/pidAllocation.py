from numpy import random
import logging
import threading
import time
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class Process:
    def __init__(self):
        self.id = self.allocate_pid()

    # generates a random pid, checks if its within range and if its already in use
    # if not in use, allocates the pid; otherwise checks next possible integer(+1)  
    def allocate_pid(self):
        NEW_PID = random.randint(self.MIN_PID, self.MAX_PID)
        inserted=False
        if(NEW_PID>=self.MIN_PID and NEW_PID<=self.MAX_PID):
            while inserted==False:
                if not self.PIDS_IN_USE.__contains__(NEW_PID):
                    self.PIDS_IN_USE.append(NEW_PID)
                    inserted=True
                else:
                    NEW_PID+=1
        else:
            print("ERR: ID %s NOT WITHIN RANGE!" %(NEW_PID))
        return NEW_PID

    # checks if pid to release is in use. if it is, releases it
    def release_pid(int_pid):
        if(Process.PIDS_IN_USE.__contains__(int_pid)):
            Process.PIDS_IN_USE.remove(int_pid)
        else:
            print("ERR: NO PROCESS RUNNING ON ID %s!" %(int_pid))

    # allocates the structure holding the pids, in this case just a simple array
    def allocate_map():
        return []

    # sets allowed range (300, 5000)
    MIN_PID = 300
    MAX_PID = 5001

    PIDS_IN_USE = allocate_map()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class Thread:
    def __init__(self):
        running_time = random.randint(1,31)
        pid = Process()
        self.runProcess(pid, running_time)
    
    # mock runs each pid for a random amount of time, max 30 seconds
    # after which it releases the pid.
    def runProcess(self, process, running_time):
        def thread_function(pid):
            time.sleep(running_time)
            Process.release_pid(pid)
            logging.info("PID %s: released.", pid)
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        x = threading.Thread(target=thread_function, args=(process.id,))
        x.start()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# testing:
print("100 threads made and running for max 30 seconds...")
i=0
while i!=100:
    Thread()
    i+=1

