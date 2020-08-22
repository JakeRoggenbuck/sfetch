import os
from termcolor import colored

[print(colored("█", 'green'), os.uname()[i]) for i in [0, 1, 2, 4]]
