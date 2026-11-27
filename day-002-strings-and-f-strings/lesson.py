"""Day 2: Strings and f-Strings (Python Foundations)"""

name, score = "Ada", 92.456
print(f"{name} scored {score:.1f}%")
s = "  Data Engineering  "
print(s.strip().lower().replace(" ", "-"))
print(s.split(), "data" in s.lower())
print("-".join(["a", "b", "c"]))
