
# - - - - IN-BUILT IMPORTS
import sys, os
from traceback import format_exc
from shutil import copy2

# - - - - RUN SCRIPT
def build():

    return


def ironpython_active():

    try:
        import clr
        return True
    except ImportError:
        return False

# - - - - RUN SCRIPT

if __name__ == "__main__":
    
    if not ironpython_active():
        raise SystemError("IronPython is not running.")
    
    args = sys.argv[1:]

    if len(args) != 2:
        raise SyntaxError("Script takes 2 arguments. {} provided.".format(len(args)))

    else:
        source_dir = args[0]
        plugin_name = args[1]

        print("The Source Folder is: {}\nThe Plugin-Name is: {}".format(source_dir, plugin_name))
