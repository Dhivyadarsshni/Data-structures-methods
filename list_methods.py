list=[16,23,32,'dhivya','darsshni',True,False,3.2,5.7]            #creating the list with all data types as an example

##########List Methods##########

                                                                  #to run a particular method : do comment other methods!

#append()-adds the element to the end of the list

list.append('chennai')                                            #appending a string

print(list)

#copy()-returns a copy of a list

list_copy=list.copy()                                             #creates an copy of list and saves in list_copy

print(list_copy) 

#clear()-removes all the elements of the string

list_copy.clear()                                                 #clears the 'list_copy' list 

print(list_copy)                                                  #it returns blank list as it is cleared in the above method

#count()-Returns the number of elements of the list

x=list.count('dhivya')                                            #returns the no. of times the element saved in the list 

print(x)

#extend()-add the elements of the list to end of the current list

numbers=[1,2,3,4,5]                                               #creating a new list

list.extend(numbers)                                              #extending the above list 'numbers' to 'list'

print(list)

#insert()-adds the element at the specified position of the list
 
list.insert(5,'girl')                                              #inserting the str'girl' in 5th index

print(list)
           
#index()-returns the index of the list

y=list.index('dhivya')                                              #returns the index of the str'dhivya'

print(y)

#pop()-removes the last element of the list

list.pop()

print(list)

#remove()-removes the item with specified value

list.remove('girl')

print(list)

#reverse()-Reverses the order of the list

list.reverse()

print(list)

#sort- sorting :ascending by default

list_str=['dd','harshu','pavi','sabi','preethi','dharani']              #creating a new list for sorting

list_str.sort()

print(list_str)

#sort(reverse=True) sorting by descending

list_str.sort(reverse=True)

print(list_str)







