#!/usr/bin/env python3
import argparse
import logging
from gnuscreen import gnuscreen_logger, GnuScreen


def main():
    logging.basicConfig()
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', '--loglevel', default='WARN', help="Python logging level")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list',action='store_true', help="List screens")
    group.add_argument('--start',help="Start screen if necesary")
    group.add_argument('--query',help="Test for existing screen")
    group.add_argument('--close',help="Close screen if it exits")
    group.add_argument('--execute',nargs='*',help="Execute commands on screen")

    args = parser.parse_args()
    gnuscreen_logger.setLevel(getattr(logging,args.loglevel))
    if args.list:
        for gs in GnuScreen.list():
            print(gs)
    if args.start:
        print(GnuScreen.get(args.start))
    if args.query:
        print(GnuScreen.query(args.query))
    if args.execute:
        name = args.execute[0]
        commands = args.execute[1:]
        gs = GnuScreen.get(name)
        gs.execute(commands)
    if args.close:
        if (gs:=GnuScreen.query(args.close)) is not None:
            gs.close()
        else:
            print(f'{args.close} not found')



if __name__ == "__main__":
    main()

