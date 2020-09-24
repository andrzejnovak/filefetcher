import os
import json
import argparse
import pprint

fset = []
with open("list.txt") as fp: 
    lines = fp.readlines() 
    for line in lines: 
        fset.append(line)

fdict = {}

xrd = 'root://xrootd-cms.infn.it//'
for dataset in fset:
    flist = os.popen(f"dasgoclient -query='file dataset={fset[0]}'").read().split('\n')
    fdict[dataset] = [xrd+f for f in flist if len(f) > 1]

#pprint.pprint(fdict, depth=1)
with open('datasets.json', 'w') as fp:
    json.dump(fdict, fp, indent=4)