import os
import sys

ping_command = f"ping {sys.argv[1]}"

ping_output = os.popen(ping_command).read()

if "TTL=" in ping_output:
  print("UP !")
else:
  print("DOWN !")
