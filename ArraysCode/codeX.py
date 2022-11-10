import numpy as np

zahlenListe=[]	# zahlenListe wird als Array definiert
N=12
for i in range(1,N+1):
  zahlenListe.append(i**2)
  print(i,zahlenListe[i-1])
print('erstes Ergebnis:', sum(zahlenListe))

neueListe = np.arange(1,N+1) # Zahlenliste wird in numpy array konvertiert
neueListe = np.square(neueListe);
print ('pythonic Ergebnis',neueListe.sum())
# neueListe = np.power(neueListe,2); 

