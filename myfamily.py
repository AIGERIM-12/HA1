import os
os.system("cls" if os.name=="nt" else "clear")
myfamily = ("mother", "father", "sister", "brother", " little sister")
print("Family members:",myfamily)
print(type(myfamily))  
print("First sister:",myfamily[2]) 
print("Second sister:",myfamily[4])
#myfamily.append("me")   append() doesn't work on tuples,it works on lists.
myfamily = myfamily + ("me",)
print("After adding 'me':", myfamily)
# myfamily.pop("brother")  pop() works on lists, not tuples.
family_list = list(myfamily)
if "brother" in family_list:
    family_list.remove("brother")  
    myfamily = tuple(family_list) 
    print("After removing 'brother':", myfamily)
else:
    print("No 'brother' found in the family.")
