#!/usr/bin/env python

import os, sys

print open(os.environ['req'], 'r').read()

with open(os.environ['res']) as res:
    res.write('ololololo')
