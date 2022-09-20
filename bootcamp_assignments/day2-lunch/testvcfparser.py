#!/usr/bin/env python

import sys

def vcf_parser(fname):
    try:
        fs = open(fname)
    except: 
        raise filenotfounderror("no file by that name")
    vcf = []
    for line in fs:
        if line.startswith('#'):
            continue
        fields = line.rstrip().split('\t')
        vcf.append(fields)
    return vcf

if __name__ == "__main__":
    vcf = vcf_parser(sys.argv[1])
    print(vcf[0][:12])
    
