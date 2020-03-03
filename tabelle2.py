bar = "-" * 17
string_template = "|{:>3}|{:>3}|{:>3}|{:>3}|"
a = 1
b = 2
c = 3

a1 = 1
a2 = 2
a3 = 3

a1a = a1 * a
a1b = a1 * b
a1c = a1 * c

a2a = a2 * a
a2b = a2 * b
a2c = a2 * c

a3a = a3 * a
a3b = a3 * b
a3c = a3 * c

print(bar)
print(string_template.format(0, a, b, c))
print(bar)
print(string_template.format(a1, a1a, a1b, a1c))
print(bar)
print(string_template.format(a2, a2a, a2b, a2c))
print(bar)
print(string_template.format(a3, a3a, a3b, a3c))