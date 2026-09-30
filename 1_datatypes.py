# None data types are used to store empty or null values.
nothing = None
print(nothing)

# single value data types store only single values
#-- numeric data types store numbers
#----- integers store whole numbers
age = 19

#---------floats store numbers with decimals
height = 5.11
print('Age:',age)
print('Height:',height)

#------- strings store texts data
name = "Hammad"
print('Name:',name)

#--------- Date and time data types store date and time
date_of_birth = "1800-09-24"
print('Date of Birth:',date_of_birth)

#------ multi value data types store multiple values
#-- lists store multiple, mutable values and allows duplicates
your_friends = ["Ali","Ahmed","hakimi",20, 70.6]
print('Your Friends:',your_friends)

#----- tuples stores multiple, immutable values and allows duplicates
never_change = ("gender","blood group","genotype")
print('Never Change:',never_change)

#----- sets store multiple, mutable values and does not allow duplicates
unique_values = {"apple", "banana", "cherry", "apple"}
print('Unique Values:',unique_values)

#---- boolean data types store true or false values
is_student = True
print('Is Student:',is_student)
