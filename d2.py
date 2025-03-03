name = "  hellop"
print(name.lower())
print(name.upper())
print(name.split("l"))
print(name.find("p"))
print(name.strip())
print(name.replace("p","o"))
print(name.isalpha())
print(name.isalnum())
print(len(name))
print("" in name)
print(name[1:7])
h = False
k = True
print(all([h,k]))
num = complex(2,9)
print(num.real,num.imag) 
print(round(5.565,2),round(5.4)) 
from enum import Enum
class state(Enum):
    Inactive=0
    active=1
print(state.active.value)
print(list(state))