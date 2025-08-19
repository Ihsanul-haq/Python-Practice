import re
name = input("what's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last,first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")