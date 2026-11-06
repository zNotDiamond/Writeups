import re
import sys

text = sys.stdin.buffer.read().decode("utf-8")
lines = text.split("\n")

# only #tags separated by spaces
tag_line = re.compile(r"^\s*(#[^\s#]+\s*)+$")

i = 0
while i < len(lines) and tag_line.match(lines[i]):
    i += 1

# if tags got removed then we strip the lines after that 
if i:
    while i < len(lines) and not lines[i].strip():
        i += 1

sys.stdout.buffer.write("\n".join(lines[i:]).encode("utf-8"))