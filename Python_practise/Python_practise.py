print("Hello World")
#Declaring a list
counties = []
counties = ['Arapahoe', 'Denver', 'Jefferson']
print(counties)

#Indexing a list - (items in list are access using indexing)
print(counties[0])
print(counties[2])

#Finding the length of a list - (function: len(list_name))
len(counties)
print(len(counties))

#Slicing a list - list_name[start:end]
counties[0:2]
print(counties[0:2])
print(counties[1:3])
print(counties[0:3])

#Add item to a list  - list_name.append()
counties.append('El Paso')
print(counties)

#To specify where in a list to add an item - "list_name.insert(index, item)"
counties.insert(2, 'El Paso')
print(counties)

#To remove an item from a list - "list_name.remove{'item')"
counties.remove('El Paso')
print(counties)

#Remove an item in a specidied index from a list - "list_name.pop(index)"
counties.pop(3)
print(counties)

#Change an item in a list to another item - "list_name[index] = 'new_item'"
counties[2] = 'El Paso'
print(counties)

#Tuple is like a lis except once created, it cannot be changed - #
# To create an empty tuple use following syntax;
# tuple_name =('items'), or
# tuple_name = tuple()
counties_tuple = ()
counties_tuple = ('Arapahoe', 'Denver', 'Jefferson')
print(counties_tuple)

# length of a tuple
len(counties_tuple)
print(len(counties_tuple))
#To get an item from a tuple, we can apply slicing & indexing, using square brackets after the tuple, just like with list


#A python dictionary has a key-value pairs enclosed in a set of curly braces {} i.e
# {key:value}
#If there is more than one key-value pair, thay are separated by commas i.e.
# {key1:value1, key2:value2, etc.}
#Rules of python dictionaries;
# 1. Values can be objects of any type including a list
# 2. Keys cannot be a list or any other type of mutable objects
#To create a python dictionary use function;
# 1. dictionary_name = {} or
# 2. dictionary_name = dict()
counties_dict ={}
counties_dict['Arapahoe'] = 422829
counties_dict['Denver'] = 463353
counties_dict['Jefferson'] = 432438
print(counties_dict)

#Length of a dictionary
len(counties_dict)
print(len(counties_dict))

#Get all keys & values of a dictionary - "dict_name.items()"
counties_dict.items()
print(counties_dict.items())

#To get all the keys of a dictionary - "dict_name.keys()"
counties_dict.keys()
print(counties_dict.keys())

#To get all the values of a dictionary - "dict_name.values()"
counties_dict.values()
print(counties_dict.values())

#To get a specific value in a dictionary - "dict_name.get('Key')" i.e
counties_dict.get('Denver')
print(counties_dict.get('Denver'))
# or you can use "dict_name['key']" i.e 
counties_dict['Arapahoe']
print(counties_dict['Arapahoe'])

#To create a list of dictionaries in which same keys are associated with different values i.e
#[{key1:value1, key2:value2}, {kei1:value3, key2:value4}, etc.]
# to create an empty list of dictionary - "list_of_dict_name = []" i.e
voting_data = []
#Then add/append each dictionay to the list of dictionaries - ""list_of_dict_name.append({dict})" i.e
voting_data.append({'county':'Arapahoe', 'registered_voters':422829})
voting_data.append({'county':'Denver', 'registered_voters':463353})
voting_data.append({'county':'Jefferson', 'registered_voters':432438})
print(voting_data)

#Add 'El Paso' & its registered voters, 461149 to the second position in voting_data
voting_data.insert(1, {'county':'El Paso', 'registered_voters':461149})
print(voting_data)

#Remove 'Arapahoe & its registered voters from voting_data
voting_data.pop(0)
print(voting_data)

#Make 'Denver' & its registered voters the third item in voting_data, but keep 'Jefferson' second
voting_data[2] = ({'county':'Denver', 'registered_voters':463353})
voting_data[1] = ({'county':'Jefferson', 'registered_voters':432438})
print(voting_data)

#Add 'Arapahoe' & its registered voters to voting_data
voting_data.append({'county':'Arapahoe', 'registered_voters':422829})
print(voting_data)


