#!/usr/bin/python3


# Local Imports
from .console import get_terminal_width



# Main pb (ProgressBar) Class
class pb():
    def __init__(self, iterable, info="", bar_console_ratio=0.3):
        self.iterable = iterable
        self.len = len(iterable)
        self.info = info
        self.width = int(get_terminal_width()*bar_console_ratio)
    

    def __iter__(self):
        self.index = 0
        return self

    
    def __next__(self):
        try:
            item = self.iterable[self.index]
            self.update()
            self.index += 1
            return item
        except IndexError:
            raise StopIteration
    

    def update(self):
        string_to_print = "\r" + str(self.info) +" "+ self.create_bar()
        
        # print the ProgressBar
        print( string_to_print, end="", flush=False )
        return
    

    def create_bar(self):
        total = self.len
        current = self.index

        current_progress = str(current) + "/" + str(total)

        done = (self.index/self.len)*self.width
        pbar = [ ("\u2588" if done>x else "\u2800") for x in range(self.width) ]

        pbar = "".join(x for x in pbar)

        bar =  "|" + pbar +"| "+ current_progress
        return bar
