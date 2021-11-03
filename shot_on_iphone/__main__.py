import argparse
import os
import sys
args = argparse.ArgumentParser(prog=f'{sys.executable.split("/")[-1]} -m shot_on_iphone', description='Shot on iphone meme maker')
args.add_argument('-i', help='input file')
args.add_argument('-o', help='Output file')
args.add_argument('-t', help='threads', type=int, default=1)
arg = args.parse_args()
if not(arg.i and arg.o):
    os.system(f'{sys.executable} -m shot_on_iphone --help')
    sys.exit(1)

try:
    from . import Iphone
    Iphone(arg.i).save(arg.o, threads=arg.t)
except OSError:
    sys.stderr.write('[?] File not found\n')
    sys.stderr.flush()
    sys.exit(1)
except AssertionError:
    sys.stderr.write('[?] Video < 20 seconds not allowed\n')
    sys.stderr.flush()