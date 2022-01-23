from time import sleep
from datetime import datetime
import multiprocessing

# square function


# Process class

class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id

    def run(self):
        sleep(1)
        time = datetime.now()
        time = time.timestamp()
        print(int(time))
        print("I'm the process with id: {}".format(self.id))


if __name__ == '__main__':
    p = Process(0)

    # Create a new process and invoke the
    # Process.run() method
    p.start()

    # Process.join() to wait for task completion.
    p.join()
    p = Process(1)
    p.start()
    p.join()
