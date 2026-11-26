"""Day 1: Variables and Types (Python Foundations)"""

age = 25
price = 19.99
name = "Ada"
is_student = True
for v in (age, price, name, is_student):
    print(repr(v), type(v).__name__)
print(int("42") + 1, float("3.5") * 2, str(10) + "!")
