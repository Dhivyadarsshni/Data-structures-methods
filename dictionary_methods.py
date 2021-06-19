dict={                                                  #creating a dictionary with three keys and their values
      "Name":"Dhivya",
      "Age":17,
      "Place":"Chennai"      
      }

print(dict)

##########Dictionary Methods##########

#do comment other methods ,if you want to access a particular method

#copy()-returns a copy of the dictionary

dict_2=dict.copy()                                           #'dict_2' is the new dictionary created to store the copy of 'dict'

print(dict_2)

#clear()-Removes all the elements from the dictionary

dict_2.clear()                                              #it clears all the keys and values of dict_2

print(dict_2)

#fromkeys()-Returns a dictionary with the specified keys and value

x = ('key_1', 'key_2', 'key_3')                             #creating a dictionary's variable x and setting its keys

y = 3                                                       #alloting the same values as '3'

dict_2 = dict.fromkeys(x, y)                                #accessing the method with x and y as parameters

print(dict_2)

#get()-Returns the value of the specified key

y=dict.get("Age")                                           #getting values from dict

print(y)

                                 
z=dict.get("location","porur") #another eg                  #we can also create temporary keys and values to access

print(z)

#items()-	Returns a list containing a tuple for each key value pair

a=dict.items()                                             #calling the items

print(a)


#keys()	-Returns a list containing the dictionary's keys

b=dict.keys()

print(a)

#pop()-	Removes the element with the specified key

dict.pop("Place")                                         #it removes the key and values as in parameter

print(dict)

#popitem()-	Removes the last inserted key-value pair 

dict_2.popitem()

print(dict_2)

#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified valued key-value pairs

c=dict.setdefault("Fav_colour","Black")                  #inserting a new key(temporarily)

print(c)

#update()-Updates the dictionary with the specified key-value pairs

dict.update({"Fav_colour":"Black"})                    #updating a key permanently

print(dict)

#values()-	Returns a list of all the values in the dictionary

d=dict.values()                                        #printing only values

print(d)


