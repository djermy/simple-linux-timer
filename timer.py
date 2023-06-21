#!/usr/bin/env python3

import os, sys
import time as t

def alert():
    return os.system('spd-say "attention, your timer has finished"')

def timer(arg):
    minutes = arg * 60
    os.system(f'spd-say "your timer has been set for {str(arg)} minutes"')
    t.sleep(minutes)
    alert()

def validate_argument():
    try:
        arg = sys.argv[1]
        arg = float(arg)
        if arg == 0.0:
            print('error! 0 is not valid')
            return None
        if arg == None:
            print('error no number given')
        return arg
    except:
        print('invalid input, must be a number')
        return None

def main():
    arg = validate_argument()
    if arg == None:
        print('error')
        return 0
    timer(arg)
    return 0

if __name__ == '__main__':
    sys.exit(main())