# zahlenListe wird als leeres Array initialisiert
zahlenListe = []
N = 12

for n in range(1, N+1):
  zahlenListe.append(n**2)

print(sum(zahlenListe))
