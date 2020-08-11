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
        print( string_to_print, end="", flush=True )
        return
    

    def create_bar(self):
        total = self.len
        current = self.index

        current_progress = str(current) + "/" + str(total)

        done = (self.index/self.len)*self.width

        # Define unicode block characters
        blank_block         = "\u2800"
        one_eight_block     = "\u258F"
        one_four_block      = "\u258E"
        three_eight_block   = "\u258D"
        half_block          = "\u258C"
        five_eight_block    = "\u258B"
        three_four_block    = "\u258A"
        seven_eight_block   = "\u2589"
        full_block          = "\u2588"


        pbar = [(full_block         if done>x       else
                 seven_eight_block  if done>x-(7/8) else
                 three_four_block   if done>x-(3/4) else
                 five_eight_block   if done>x-(5/8) else 
                 half_block         if done>x-(4/8) else
                 three_eight_block  if done>x-(3/8) else
                 one_four_block     if done>x-(1/4) else
                 one_eight_block    if done>x-(1/8) else
                 blank_block)
                 
                 for x in range(self.width) ]


        pbar = "".join(x for x in pbar)

        bar =  "|" + pbar +"| "+ current_progress
        return bar
