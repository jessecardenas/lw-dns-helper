#!/usr/bin/python3
import argparse, pprint, sys
from lw_helper import *

# lw_api_browser
#  A quick and dirty api exploration tool
#
# Issues:
# Todo:
#  Basic framework
#  Auth
#  Parser
# In progress:
# Done:

parser = argparse.ArgumentParser(description='LW API helper.')
parser.add_argument('action', choices=['ls','cat','rm'], help='Action to take')

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

pprint.pprint(args.__dict__)

path = args.path.strip('/').split('/')

done = False



