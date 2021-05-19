
import json


#Read JSON data into the datastore variable

with open('C:/Ralph/PXL/2020-2021_EA/Project Engineering/Code1Servo/test.json', 'r') as f:
    datastore = json.load(f)

#Use the new datastore datastructure
print (datastore["office"]["parking"]["style"])