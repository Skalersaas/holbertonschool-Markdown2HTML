#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """

import sys
import os
def Heading(line):
    count = line.count('#')
    return "<H"+str(count)+">"+line[count:]+"</H"+str(count)+">"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        text = open(sys.argv[0],"r")
        lines = text.splitlines()
        HTML = ""
        
        for line in lines:
            if(line[0]=='#'):
                HTML += Heading(line)

        htmlfile = open(sys.argv[1],"w")
        htmlfile.write(HTML)
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)
    exit(0)
