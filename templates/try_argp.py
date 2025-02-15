#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(
    description='Just a test script man',
    epilog = 'A section or speech at the end of a book or play that serves as a comment on or a conclusion to what has happened.'
)
parser.add_argument('pattern',help='Substring pattern to match, not really.')
parser.add_argument('path',help='Dumb neighbors upstairs')
parser.add_argument('-p','--prefix',default='',help='pak man pak')


if __name__ == '__main__':
    args = parser.parse_args()
    if args.pattern:
        print(args.pattern)
    if args.prefix:
        print(args.prefix)



# -ugh, stupid neighbor
