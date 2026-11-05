import sys

# On lit (et on jette) le vrai contenu du fichier
sys.stdin.buffer.read()

# On affiche le placeholder à la place
with open(".meta/flag-placeholder.md", "rb") as f:
    sys.stdout.buffer.write(f.read())