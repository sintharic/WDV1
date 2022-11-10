i=1
N=12
summe = 0
stateOfMind=False

while (stateOfMind==False):
# alternativ: while not stateOfMind:
  summe += i*i
  if (i==N): 
    stateOfMind=True
    # alternativ: break
  i += 1

print(i,summe)
