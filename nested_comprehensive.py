from random import randint
from pprint import PrettyPrinter

keys = range(1,5)
values = range(10,41,10)
print('keys:',[key for key in keys])
print('values:', [value for value in values])

###zip into tuples
##tuple_list = zip(keys,values)
##print('list of tupels:',[pair for pair in tuple_list])

zip_keys, zip_values =zip(*zip(keys,values))
print('zip_keys: ',zip_keys)
print('keys from zip',[key for key in zip_keys])
print('zip_values: ',zip_values)
print('values from zip',[value for value in zip_values])


###### Zip the keys and values into a Dict######
dict_zip=dict(zip(values,keys))
