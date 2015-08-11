import sys

class pcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    GRAY = '\033[1;30m'
    ENDC = '\033[0m'
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    
def ok():
    sys.stdout.write(pcolors.OKGREEN)
    sys.stdout.flush()

def comment():
    sys.stdout.write(pcolors.GRAY)
    sys.stdout.flush()

def err():
    sys.stdout.write(pcolors.FAIL)
    sys.stdout.flush()

def blue() :
    sys.stdout.write(pcolors.OKBLUE)
    sys.stdout.flush()

def end() :
    sys.stdout.write(pcolors.ENDC)
    sys.stdout.flush()

def msg_ok(*messages):
    ok()
    for message in messages:
        print message
    end()

def msg_err(*messages):
    err()
    for message in messages:
        print message
    end()