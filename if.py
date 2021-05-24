x = 2
if x < 0:
  x = 0
  stri = 'Negative changed to zero'
elif x == 0:
  stri = 'Zero'
elif x == 1:
  stri = 'Single'
else:
  stri = 'More than one'
print(stri)
