#!/usr/bin/python
import sys
import re
with open(sys.argv[1], 'r') as f:
    for line in f:
       line = re.sub(r'<.*?>', "", line)  # Regex
       line=line.rstrip()  # strips the line break
       if len(line) > 0:  # insures that there is some text in line
          print line
