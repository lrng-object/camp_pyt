#1)
some_string = "I'm a string"
some_number = 13
some_boolean = True
some_list = [1,2,3,4,5] 

#2)
first_three_letters = some_string[ : 3]
print(first_three_letters)

#3)
first_element = some_list[0]
print(first_element)

#4)
new_number = some_number + 10
print(new_number)

#5)
last_element = some_list[-1]
print(format(last_element))

#6)
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)

#7)
index_rest = some_string.index(" ")
first_word = some_string[ : index_rest].upper()
new_string =  first_word + some_string[index_rest : ]
print(new_string)

#8)
print(f"Total: {some_number}")
print("Total: {0}".format(some_number))

#9)
print('"hello world"')