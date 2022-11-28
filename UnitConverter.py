convalue = {
    'cm':2.54,
    'm':.0254,
    'ft':1/12,
    'mi':1/63360,
    'furlongs':1/7920,
    'yards':1/36
    }

convalue_parse = ', '.join(convalue)

print('Enter the unit to convert inches to: \n',convalue_parse)

while True:
    selunit = input()
    if selunit.lower() in convalue:
        break
    print('Please enter a supported unit: \n',convalue_parse)

convfactor = convalue[selunit.lower()]

while True:
    print('How many inches need converted?')
    unitval = input()
    try:
        unitval = float(unitval)
    except:
        print('> Enter a numeric value.')
        continue
    if unitval <= 0:
        print('> Enter a nonzero, positive numeric value.')
        continue
    break

print(str(unitval) + ' inches is ' + str(convfactor * unitval) + ' ' + selunit.lower())