## dictionary and set

#dictionary is as like js object ar moto

person ={
  'name': "gowtam kumar",
  "age": 30,
  'learning': ["python", 'react,js', "nodejs"]
}

person["name"] = "Poly Rani" # update data from disctionary
person["sub"] = "js" # add data in disctionary
person["newArr"] = ["js", 'sql'] # add data in disctionary

# print(person) # access

# print(person.keys()) ## return all keys
# print(person.values()) ## return all values
# print(list(person.values())) ## return all values by list as like js array

# print(person.items())  # return all (key, val) pairs as tuples
# print(person.get('name')) ## return the key according to value
# person.update({'age': "Jashore"}) ## new add  and update element in distinoray

# print(person)

## set as dont store duplicate value
  # u can not add list type data

collection ={4, 3,4 ,5, 'gowtam kuamr', 30,}
print(len(collection)) #return len

newColleciton = set() # empty dictionary 

newColleciton.add(2) # add element
newColleciton.add(5) # add element
newColleciton.add(6) # add element
newColleciton.add((2,3,4)) # add element
newColleciton.add("gowamkumar") # add element

# print(newColleciton)

# newColleciton.remove(2) # remove element

# print(newColleciton)

# newColleciton.clear() # return the all set
# print(newColleciton)

# example = {"hello", "orange", "world"}
# example.pop() # ramdom value remove
# print(example)

# union example this union example
example = {'poly', 'arko'} 
example2 = {'gowtam', 'arko'}
print(example.union(example2))
## intersection 
print(example.intersection(example2)) # return duplicate value
