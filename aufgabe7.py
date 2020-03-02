n = 5
string_template = "|{:>3}|{:>3}|{:>8}|"
horizontal_bar = "-" * 18
print(horizontal_bar)
print(string_template.format("a","b","ergebnis"))
print(horizontal_bar)
for a in range(1,n+1):
    for b in range(1,n+1):
        ergebnis = a * b
        print(string_template.format(a, b, ergebnis))
print(horizontal_bar)
