#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as file:
    content = file.readlines()

    for line in content:
        old_name = line.strip()
        new_name = old_name.replace('mesg', 'msg')
        command = ["mv", old_name, new_name]
        output = subprocess.run(command, capture_output=True)
        print(output.stdout)
