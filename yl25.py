mina = {
  "Eesnimi": "Robin",
  "Perenimi": "Mihkelson",
  "Sünniaasta": "2007",
  "Elukoht": "Eikla",
  "Lemmik magustoit": "Jäätis",
}

print(mina.get('Elukoht'))

mina['Lemmik magustoit'] = 'Jäätis'

mina['height'] = '1.80'

del mina['Sünniaasta']

mina.clear()

for s, r in mina.items():
    print(s, r)

#me['personal_code'] = '12345678910'

if 'personal_code' in mina:
    print(mina['Isikukood on dictionaris '])
else:
    print('Isikukood ei ole dictionaris')

print(len(mina))
