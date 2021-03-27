#DECISION STATEMENTS
#There are 2 types of decision statement;
# 1) 'if' statements, and
# in this statement, if a condition is met, then an action is perfomed, otherwise the action is not performed
#General format for 'if' statements in python is;
# if condition:
#    statement 1
#    statement 2 i.e
if counties[1] == 'Denver':
    print(counties[1])

# 2) 'if-else' statements
#Refered to as 'dual alternative decision statement', 'if-else' will execute an action if a condition is met  or another action if the condition is not met
#General format for 'if-else' statements in python is;
# if condition:
#    statement 1
#    statement 2 
# Else:
#    statement 1
#    statement 2  i.e.
if counties[1] != 'Denver':
    print(counties[1])
else:
    print(counties[0])

#NESTED IF-ELSE STATEMENTS
#When a decision structure is more complex than a dual alternative decision structure, we can nest decision structures inside another decision structure

#NESTED IF-ELSE STATEMENTS (if-elif-else)
#When a decision structure is more complex than a dual alternative decision structure, we can nest decision structures inside another decision structure

#What is the core?
score = int(input('What is your test score?'))
#Determine grade
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >=60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')
