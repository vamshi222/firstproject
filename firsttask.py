import math as m #Math related functions

class vamshi:   
    
    def my_func(self, number):
         j = 1
         while (j < number+1):
             print(j)
             j+=1
    def string(self, value, length):
        print(value[0])
        print(value[m.ceil(length/2)])
        print(value[length-1])
        


obj = vamshi()
num = int(input("Enter the nth number:"))
obj.my_func(num)
value = input("Enter a String:")
length = int(len(value))
obj.string(value, length)
