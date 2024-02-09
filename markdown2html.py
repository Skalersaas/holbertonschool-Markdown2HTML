#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """

import sys
import os
def Heading(line):
    count = line.count("#")
    helper = "<H"+str(count)+">"
    return helper+line[count:]+helper.replace("<","</")

def UL(lines):
    html = "<ul>"
    for line in lines:
        if(line[0]=="-"):
            html += "<li>"+line[:1]+"</li>"
            lines.remove(line)
        else: break
    html += "</ul>"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)


    with open(sys.argv[1]) as MD:
        with open(sys.argv[2],'w') as HTML:
            lines = MD.read()
            html = ""

            UL = False
            for i in range(len(lines)):
                line = lines[i]
                if(line[0]=="#"):
                    html += Heading(line)
                if(line[0]=="-"):
                    html += UL(lines[i:])

            HTML.write(html)
    exit(0)
