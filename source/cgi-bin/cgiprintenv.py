#!/usr/bin/env python3

import os
from sys import stdout

stdout.write("Content-type: text/plain\r\n\r\n")

for key in sorted(os.environ.keys()):
    print("%s=%s" % (key, os.environ[key]))
