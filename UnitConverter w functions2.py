
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

convalue_parse = ', '.join(metric_convalue|imperial_convalue)
in_to_cm = 2.54
cm_to_in = 1/2.54

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
def conversion_type():
    global to_imperial
    global from_imperial
    while True:
        if selunit_to.lower() in metric_convalue:
            to_imperial = False
            break
        if selunit_to.lower() in imperial_convalue:
            to_imperial = True
            break
    while True:
        if selunit_from.lower() in metric_convalue:
            from_imperial = False
            break
        if selunit_from.lower() in imperial_convalue:
            from_imperial = True
            break
def validate_value():
    while True:
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
def validate_unit(selunit):
    valid_unit = selunit.lower() in metric_convalue or selunit.lower() in imperial_convalue
    global validated_unit
    validated_unit = selunit
    while valid_unit != True:
        print('Please enter a supported unit: \n',convalue_parse)
        new_unit = input()
        valid_unit = new_unit.lower() in metric_convalue or new_unit.lower() in imperial_convalue
        validated_unit = new_unit

print('Enter the unit to convert from: \n',convalue_parse)
selunit_from = input()
validate_unit(selunit_from)
selunit_from = validated_unit.lower()

print('Enter the unit to convert >' + selunit_from + '< to: \n',convalue_parse)
selunit_to = input()
validate_unit(selunit_to)
selunit_to = validated_unit.lower()

print('How many >' + selunit_from + '< need converted?')
validate_value()
conversion_type()
conversion(unitval)

print(str(unitval) + ' ' + selunit_from.lower() + ' is ' + str(finalval) + ' ' + selunit_to.lower())