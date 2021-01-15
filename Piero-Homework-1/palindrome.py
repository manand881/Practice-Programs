Input_String=input("Enter a String : ")

#   Solution 1

if Input_String==Input_String[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#   Solution 2

Str_list=list()
for x in range(len(Input_String)):
    Str_list.append(Input_String[x:x+1])

while len(Str_list)>1:
    if Str_list[0]==Str_list[-1]:
        Str_list.pop(0)
        Str_list.pop(-1) 
    else:
        print("Not a palindrome")
        break

if len(Str_list)==1 or len(Str_list)==0:
    print("Palindrome")

#   Solution 3

Str_list=list()
for x in range(len(Input_String)):
    Str_list.append(Input_String[x:x+1])

Str_list_2=Str_list.reverse()
if Str_list==Str_list_2:
    print("Palindrome")
else:
    print("Not a palindrome")