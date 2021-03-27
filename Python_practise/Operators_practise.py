#MEMBERSHIP OPERATORS

# 2 Types of membership operators
# 1) 'in' - returns true if a sequence with a specified value is present in an expressio/list/tuple/dictionary, otherwise, it returns false
# 2) 'not in' - returns true if a sequence with specified value is not present n an expressio/list/tuple/dictionary, otherwise, it returns false

counties = []
counties = ['Arapahoe', 'Denver', 'Jefferson']
print(counties)

if 'El Paso' in counties:
    print('El Paso is in the list of counties')
else:
    print('El Paso is not in the list of counties')

#LOGICAL OPERATORS
# This allows to connect multiple comparisson expressions to create a compound expression
# There are 3 logical operators
# 1) 'and' - evaluates 2 boolean expressions into 1 compound expression, if both expression is true. If one is false, then the compound expression is false
# 2) 'or' - evaluates 2 boolean expressions into 1 compound expression, and make it true, if either expression is true. If one is false, then the compound expression is true, but false, if both are false
# 3) 'not' - evaluates a boolean expression to be true if the condition is false
# membership & logical operators can be combined to test certain conditions

if 'Arapahoe' in counties and 'El Paso' in counties:
        print('Arapahoe and El Paso are in the list of counties')
else:
    print('Arapahoe or El Paso are not in the list of counties')

if 'Arapahoe' in counties or 'El Paso' in counties:
        print('Arapahoe or El Paso is in the list of counties')
else:
    print('Arapahoe and El Paso are not in the list of counties')

if 'Arapahoe' in counties and 'El Paso' not in counties:
        print('Only Arapahoe is in the list of counties')
else:
    print('Arapahoe is not in the list of counties and El Paso is not in the list of counties')   