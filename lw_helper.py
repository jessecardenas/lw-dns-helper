#!/usr/bin/python3
import argparse
import requests, json, pprint
import sys, os, time, datetime
import configparser
import config as c

# Issues:
# Todo:
#  Auth
#  API boilerplate function
# In progress:
#  Basic framework
#  Parser
# Done:
#

def get_args():
    """Get command line arguments"""
    p = argparse.ArgumentParser(description='LW API helper.')
    p.add_argument('--auth-test', action='store_true', help='Test authenticating with lw')
    if len(sys.argv)==1:
        p.print_help(sys.stderr)
        sys.exit(1)
    args = p.parse_args()
    return args


def lw_auth(nocache=False):
    """Fetch LW auth token"""
    pass

def main():
    """do stuff i guess"""
    args = get_args()
    if args.auth_test:
        pprint.pprint(lw_auth())


if __name__ == '__main__':
    main()

