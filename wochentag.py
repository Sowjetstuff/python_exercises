#wochentag.py
#----------------------------------------------------
#Ausgabe von Wochentag eines bestimmten Datums
#----------------------------------------------------
#Eingabe von Tag, Monat und Jahr

print("Gib das vollständige Datum ein z.B. 1.4.1999:" + "\n")
t = int(input(" Tag: "))
m = int(input(" Monat: "))
j = int(input(" Jahr: "))

#Berechnung der einzelnen Komponenten

j0 = j - (14 - m // 12)
m0 = m + 12 * (14 - m // 12) - 2
x = j0 + (j0/4) - (j0/100) + (j0//400)
t0 = ( t + x + (31*m0/12)) % 7

#Ausgabe des Wochentags
print()
print(" " + str(t0))
#print(" Das eingegebene Datum ist ein " + t0)

#----------------------------------------------------

