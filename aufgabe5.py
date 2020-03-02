print("Gib die Zahl n ein: ", end="")
n = int(input())
print()
for Zahl in range(1,n+1):
    if Zahl % 3 == 0: #or Bedingung
        print(Zahl)
    if Zahl % 5 == 0:
        print(Zahl)
