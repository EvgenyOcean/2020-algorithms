import time
class Tracker: 
    def __enter__(self): 
        self.start = time.time()

    def __exit__(self, *_):
        wasted = time.time() - self.start
        print(f'Script took {wasted}s')