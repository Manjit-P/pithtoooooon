spot = ["dog",1,"cat", 3,True,complex(3,5)]
spot [2] = "nooooo"
#print(len (spot))
spot.extend(["hell",459])    #spot += ["hell",459]
spot.remove("dog")
print(spot.pop())            #removes last item from list and returns that item
spot.insert(3,"jjajajaj")
h = ["H","b" ,"B","a","A"]
print(sorted(h,key=str.lower)) #sorts without modifying the original list
print(spot.pop())
hello = spot[1:5]
print(hello)
print(h)
print(spot)
number=[1,2,3,4]
square = [n**2 for n in number]     # list compression
print(square)                       #1, 4, 9 ,16