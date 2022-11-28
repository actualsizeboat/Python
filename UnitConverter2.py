#These dictionaries set the supported values for conversion. The base unit is arbitrarily chosen based on how common it is.
metric_convalue = {
    'mm':.1,
    'cm':1,
    'm':100,
    'km':100000,
    }

imperial_convalue = {
    'in':1,
    'ft':12,
    'mi':63360,
    'yd':36
    }

# Later conversion functions reduce the input to a base unit, which is then converted with these variables.
in_to_cm = 2.54
cm_to_in = 1/2.54
unitval = 0

# This parses the list of conversion values together to make stuff easier later.
convalue_parse = ', '.join(metric_convalue|imperial_convalue)

print('Enter the unit to convert from: \n',convalue_parse)
selunit_from = input()

## The from_imperial and to_imperial values are set at this time to use in logic later.
while True:
    if selunit_from.lower() in metric_convalue:
        from_imperial = False
        break
    if selunit_from.lower() in imperial_convalue:
        from_imperial = True
        break
    print('Please enter a supported unit: \n',convalue_parse)

print('Enter the unit to convert >' + selunit_from + '< to: \n',convalue_parse)
selunit_to = input()

while True:
    if selunit_to.lower() in metric_convalue:
        to_imperial = False
        break
    if selunit_to.lower() in imperial_convalue:
        to_imperial = True
        break
    print('Please enter a supported unit: \n',convalue_parse)

while True:
    print('How many >' + selunit_from + '< need converted?')
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

# This logic handles converting to imperial. When converting from metric to imperial, the input is first converted to cm.
while to_imperial == True:
    if from_imperial == True:
        convfrom = unitval * imperial_convalue[selunit_from.lower()]
        convto = imperial_convalue[selunit_to.lower()]
        finalval = convfrom/convto
        break
    if from_imperial == False:
        convfrom = metric_convalue[selunit_from.lower()] * unitval
        convto = imperial_convalue[selunit_to.lower()]
        finalval = cm_to_in * convfrom/convto
        break

# This logic handles converting to metric. When converting from imperial to metric, the input is first converted to inches.
while to_imperial == False:
    if from_imperial == True:
        convfrom = imperial_convalue[selunit_from.lower()] * unitval
        convto = metric_convalue[selunit_to.lower()]
        finalval = in_to_cm * convfrom/convto
        break
    if from_imperial == False:
        convfrom = unitval * metric_convalue[selunit_from.lower()]
        convto = metric_convalue[selunit_to.lower()]
        finalval = convfrom/convto
        break

print(str(unitval) + ' ' + selunit_from.lower() + ' is ' + str(finalval) + ' ' + selunit_to.lower())