import threading
import time

class ThreadManager:
    def __init__(self):
        self.threads = []

    def addThread(self, beast):
        thread=threading.Thread(target=beast.start)
        self.threads.append(thread)

    def start(self):
        for thread in self.threads:
            print("Starting thread:", thread)
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()

    def stop(self):
        for thread in self.threads:
            thread.stop()  
