import os

class Keyboard():
    quantity: int = 0

    def __init__(self):
        self.quantity += 1

    def read(self):
        """getch() for Windows and Linux.
        This won't work unless run from a terminal.
        """
        # this must be executed from a terminal

        # msvcrt library for Windows
        if os.name == 'nt':
            import msvcrt
            # clear the buffer
            while msvcrt.kbhit():
                ch_in = msvcrt.getch()
            # read keyboard
            ch_in = msvcrt.getch()
            if ord(ch_in) == 224:
                ch_in = msvcrt.getch()

        elif os.name == 'posix' or os.name == 'mac':
            import termios
            import sys
            import tty
            # LINUX uses termios and tty
            # clear buffer
            sys.stdin.flush()
            # read char
            fd_in = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd_in)
            try:
                tty.setraw(sys.stdin.fileno())
                ch_in = sys.stdin.read(1)
                if ord(ch_in) == 27:
                    ch_in = sys.stdin.read(1)
                if ch_in == '\x1b':  # alt key (27)
                    ch_in = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd_in, termios.TCSADRAIN, old_settings)
        else:
            pass

        # convert to unicode code for Python 3
        return ord(ch_in)