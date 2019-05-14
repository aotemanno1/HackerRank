vehicles = ['sedan','coupe','hatchback','wagon']
print("vehicles = ",vehicles)

cars = map(str.capitalize, vehicles)
print('Map Cars = ',cars)

cars = list(map(str.capitalize, vehicles))
print('Map Cars after list = ',cars)

cars = [car.capitalize() for car in vehicles]
print( "Capitalize in vechincle = ",cars)

def quad(val):
    return val **4
nums = range(4)
print("List of nums:", list(nums))
quads = list(map(quad,nums))
print("list of quads = ", quads)
quads = list(map(lambda val: val **4, nums))
print(quads)

def mult(x,y):
    return x*y
num_quads = list(map(mult,nums,quads))
print("numb_quads = ", num_quads)
num_quads = list(map(lambda x,y:x*y*10,nums,quads))
print("numb_quads in another way = ",num_quads)
