some_string = "I'm a string"
some_number = 13
some_boolean = True
some_list = [1,2,3,4,5] 

first_three_letters = some_string[ : 3]
print(first_three_letters)

first_element = some_list[0]
print(first_element)

new_number = some_number + 10
print(new_number)

last_element = some_list[-1]
print(format(last_element))

names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)

print(f"Total: {some_number}")
print("Total: {0}".format(some_number))

print('"hello world"')