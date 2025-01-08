#!/usr/bin/env python3

import nmap3
import optparse

nmap = nmap3.Nmap()

def nmapScan(tgtHost):
    results = nmap.scan_top_ports(tgtHost)
    print(results)

def main():
    parser = optparse.OptionParser('usage%prog -H <target host> >')
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    if(tgtHost == None):
        print(parser.usage)
        exit(0)
    else:
        nmapScan(tgtHost)

if __name__ == '__main__':
    main()
