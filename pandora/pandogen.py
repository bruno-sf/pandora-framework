#!/usr/bin/env python
import os, sys, subprocess
from time import sleep
from optparse import OptionParser

parser = OptionParser(usage="./Pandogen <var=value> \nexample: ./Pandogen --host=<host> --port=<port> --path=<path>")

parser.add_option("--host", type="string", dest="tghost", help="Specify target host")

parser.add_option("--port", type="int", dest="tgport", help="Specify target port")

parser.add_option("--path", type="string", dest="path", help="Specify payload destination")

(options, args) = parser.parse_args()

host = options.tghost
port = options.tgport
output = str(options.path)

add = ''
if not output.endswith(".py"):
    if output.endswith("/"):
        add = "payload.py"
    else:
        add = "/payload.py"



if host == None or port == None or output == None:

    parser.print_help()
else:
    print("\33[92m[*] Generating Payload . . .\33[00m")
    sleep(3)
    os.system("sh ~/pandora-framework/pandora/modules/gen.sh "+host+" "+str(port)+" "+output+add)

    print("\33[92m[+]payload Generating Success . . .\33[00m")
    print("[>]Payload generated to '{}' ".format(output + add))
    sleep(1)
