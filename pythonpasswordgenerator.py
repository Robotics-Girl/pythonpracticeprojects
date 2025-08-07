import string 
import random 
size = int(input("Give me the length of the password you want: "))
list = string.ascii_letters + string.digits + string.punctuation
id=""
for i in range(size):
    random_value = str(list[random.randint(0, len(list)-1)])
    id = id + random_value
print(id)
