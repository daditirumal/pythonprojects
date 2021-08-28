"""Load a text file as a list.

Arguments:
-text file name (and dictionary path, if needed)

Exceptions:
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import sys

"""
import sys
import os

def load_list(file):
    """Open a text file & return a list of lowercase string"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as exc:
        print("{}\nError opeming {}. Terminating program.".format(exc,file),
        file=sys.stderr)
    sys.exit(1)

