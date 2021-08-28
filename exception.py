import os
import sys
file = os.path.expanduser('~/Desktop/python_programing/python_projects/12dicts-6.0.2/American/2of12.txt')
try:
    with open(file,'r') as in_file:
        loaded_txt = in_file.read()
        loaded_txt = [x.lower() if type(x) == 'str' else None for x in loaded_txt]
        print (loaded_txt)
except IOError as e:
    print("{}\nError opeming {}. Terminating program." .format(e, file), file=sys.stderr)
    sys,exit(1)


file_to_open = os.path.expanduser('~/Desktop/movie_quotes.txt')