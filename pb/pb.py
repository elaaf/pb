# Imports
# from .console import get_terminal_width



# pb Class
class pb():
    def __init__(self, iterable, desc="", width=50, console_width_ratio=0.3):
        self.iterable = iterable
        self.len = len(self.iterable)
        self.index = 0
        self.desc = desc
        self.width = width
        if get_terminal_width():
            self.width = int(get_terminal_width()*console_width_ratio)
    

    def __iter__(self):
        return self


    def __next__(self):
        try:
            item = self.iterable[self.index]
            self.show_bar()
        except IndexError:
            self.show_bar()
            raise StopIteration
        self.index += 1
        return item
    

    def show_bar(self):
        string_to_print = "\r" + str(self.desc) +" "+ self.create_bar()
        
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