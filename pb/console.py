# Console/Terminale related functions



# Get width of the terminal
def get_terminal_width():
    """
    Returns:
    The width (columns) of the current terminal
    window
    """
    # Moved import statement inside
    import os
    return os.get_terminal_size().columns
