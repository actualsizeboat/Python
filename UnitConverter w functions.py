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

in_to_cm = 2.54
cm_to_in = 1/2.54
unitval = 0

def conversion(unitval):
    global finalval
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

def from_unit():
    print('Enter the unit to convert from: \n',convalue_parse)
    
    while True:
        global selunit_from
        global from_imperial
        selunit_from = input()
        if selunit_from.lower() in metric_convalue:
            from_imperial = False
            break
        if selunit_from.lower() in imperial_convalue:
            from_imperial = True
            break
        print('Please enter a supported unit: \n',convalue_parse)

def to_unit():
    print('Enter the unit to convert >' + selunit_from + '< to: \n',convalue_parse)
    
    while True:
        global selunit_to
        global to_imperial
        selunit_to = input()
        if selunit_to.lower() in metric_convalue:
            to_imperial = False
            break
        if selunit_to.lower() in imperial_convalue:
            to_imperial = True
            break
        print('Please enter a supported unit: \n',convalue_parse)

def validate_unit():
    while True:
        print('How many >' + selunit_from + '< need converted?')
        global unitval
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

convalue_parse = ', '.join(metric_convalue|imperial_convalue)

from_unit()

to_unit()

validate_unit()

conversion(unitval)

print(str(unitval) + ' ' + selunit_from.lower() + ' is ' + str(finalval) + ' ' + selunit_to.lower())