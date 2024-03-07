import threading
import time

class ThreadManager:
    def __init__(self):
        self.threads = []

    def addThread(self, thread):
        self.threads.append(thread)

    def start(self):
        for thread in self.threads:
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()

    def stop(self):
        for thread in self.threads:
            thread.stop()  
