import sys

sys.stdin.buffer.read()

with open(".meta/assets/nope.gif", "rb") as f:
    sys.stdout.buffer.write(f.read())