f_name = input("what is your first name?")
l_name = input("what is your last name?")
favcolor = input("what is your fav color?")
sym = input("enter you fav symbol?")
age = input("what is your age?")
shift= int(input("how many places to shift in string ?"))
output1 = ""
output2 = ""
output3 = ""
output4 = ""
for char in f_name:
    output1 += chr(ord(char)+shift)

for char in favcolor:
    output2 += chr(ord(char)+shift)

for char in l_name:
    output4 += chr(ord(char)+shift)
new_password = output1+output4+output2+sym+age
print("NEW PASSWORD=>"+" " + new_password.title())
