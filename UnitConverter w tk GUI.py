# match case for to and from?

from tkinter import *
from tkinter import ttk
root = Tk()

metric_length = {
    'mm':.1,
    'cm':1,
    'm':100,
    'km':100000,
    }
imperial_length = {
    'in':1,
    'ft':12,
    'mi':63360,
    'yd':36
    }

length_parse = ', '.join(metric_length|imperial_length)
in_to_cm = 2.54
cm_to_in = 1/2.54
unit_options = metric_length|imperial_length
to_imperial = ''
from_imperial = ''

def conversion(unitval):
    global finalval
    while to_imperial == True:
        if from_imperial == True:
            convfrom = unitval * imperial_length[from_unit.get()]
            convto = imperial_length[to_unit.get()]
            finalval = convfrom/convto
            break
        if from_imperial == False:
            convfrom = metric_length[from_unit.get()] * unitval
            convto = imperial_length[to_unit.get()]
            finalval = cm_to_in * convfrom/convto
            break

    while to_imperial == False:
        if from_imperial == True:
            convfrom = imperial_length[from_unit.get()] * unitval
            convto = metric_length[to_unit.get()]
            finalval = in_to_cm * convfrom/convto
            break
        if from_imperial == False:
            convfrom = unitval * metric_length[from_unit.get()]
            convto = metric_length[to_unit.get()]
            finalval = convfrom/convto
            break
    label.config( text = str(value_entry.get()) + ' ' + from_unit.get() + ' is ' + str(finalval) + ' ' + to_unit.get())
def conversion_type():
    global to_imperial
    global from_imperial
    if to_unit.get() == "To" or from_unit.get() == "From":
        label.config( text = 'Select a unit to convert from and to.')
    while to_unit.get() != "To":
        if to_unit.get() in metric_length:
            to_imperial = False
            break
        if to_unit.get() in imperial_length:
            to_imperial = True
            break
    while from_unit.get() != "From":
        if from_unit.get() in metric_length:
            from_imperial = False
            break
        if from_unit.get() in imperial_length:
            from_imperial = True
            break
def validate_value():
    global unitval
    unitval = value_entry.get()
    try:
        unitval = float(unitval)
    except ValueError:
        label.config( text = 'Enter a numeric value')
    except TypeError:
        label.config( text = 'Enter a numeric value')

# creates the entry box for the value
value_entry = ttk.Entry(root, textvariable='')
value_entry.pack()

# datatype and initial menu text
from_unit = StringVar()
from_unit.set( "From" )
to_unit = StringVar()
to_unit.set( "To" )

# Create Dropdown menus
from_drop = OptionMenu( root , from_unit , *unit_options.keys() )
from_drop.pack()
to_drop = OptionMenu( root , to_unit , *unit_options.keys() )
to_drop.pack()

selunit_from = from_unit.get()
selunit_to = to_unit.get()
unitval = value_entry.get()

# Create Label
label = Label( root , text = " " )
label.pack()

## write something to set button state to prevent errors
button = Button( root , text = "Convert" , command = lambda: [validate_value(),conversion_type(), conversion(unitval) ])
button.pack()


root.mainloop()