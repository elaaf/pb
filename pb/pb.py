# Imports


# pb Class
class pb():
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.iterable[self.index]
            self.bar()
        except IndexError:
            raise StopIteration
        self.index += 1
        return item
    
    def bar(self):
        total = len(self.iterable)
        print(f"\rIter:{self.index}", end="", flush=True)
        return