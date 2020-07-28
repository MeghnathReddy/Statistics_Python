#!/usr/bin/env python
# coding: utf-8

# In[6]:


#problem 1 statistics-Mean,Mode,Median
from collections import Counter
from math import sqrt
def mean(list):
    if len(list)==0: #check if length is zero
        return 0
    else:
        sum=0 #initialize the sum
        for i in list:
            sum+=i #total sum
            mean=sum/len(list) #average
        return mean

def median(list):
    if len(list)==0:  #check if length is zero
        return 0
    else:
        list.sort() #order in ascending order
        midpoint=len(list)//2 #to find middle term
        count=len(list) #to find length
        if count%2==1: #the length is odd
            median=list[midpoint]
        else: 
            median=list[midpoint]+list[midpoint-1]/2 #incase of even terms
    return median

def mode(list):
    list.sort()
    List1=[]
    i = 0
    while i < len(list) : 
        List1.append(list.count(list[i])) 
        i += 1
        d1 = dict(zip(list, List1)) 
        new_list={k for (k,v) in d1.items() if v == max(List1) }
    return new_list

def std(list):
    if len(list)==0: #check if length is zero
        return 0
    
    std_deviation = sqrt(sum([(number - mean(list)) ** 2 for number in list]) / (len(list) - 1)) #mathematical formulation
    return std_deviation

def main():
    x=int(input("Enter number of elements in list:"))
    list=[] #list to store the input from user
    for i in range(x):
        list.append(int(input("Enter element:")))
    print("Mean of the given list=",mean(list))
    print("Median value of given list=",median(list))
    print("Mode of given list=",mode(list))
    print("SD of the givem list=",std(list))
    
    
    
if __name__ == "__main__":
    main()
                  


#problem 2 Newton Method
estimate = 1.0 #initialize
tolerance = 0.001

def newton(x,estimate):
    estimate=(estimate+x/estimate)/2 #formulation
    difference =abs(x-estimate**2)
    if difference<= tolerance:
        return estimate #when difference>=estimate it prints the result
    else:
        return newton(x,estimate) #recursive call
    
x = float(input("Enter a positive number:")) #take input we can also take decimal values
print("The program's estimate:",newton(x, estimate))


#problem 3 Exponent
def expo(number,exponent):
    if(exponent==1 or exponent==0): #check if the value is 0 or 1
        return(number)
    else:
        return(number*expo(number,exponent-1)) #recursive call the exponent value follows descending order
    
number=int(input("Enter base: ")) #take input from the user
exponent=int(input("Enter exponential value: ")) #take input from the user

print("The number raised to given exponent is:",expo(number,exponent)) #passing paramters to the function

# O(2^n)is the computational complexity for exponential function


#problem 4 Fibonacci Sequence
def Fibonacci(x): 
    first_num=0 #initialize
    second_num=1 #initialize
    if x<0: 
        print("Invalid input") #it can not be negative
    elif x==0: 
        return first_num #the sequence starts with 1,1,..... 
    elif x==1: 
        return second_num #we assume the 1st term in sequence is 1
    else: 
        for i in range(2,x+1): #iterate in the range from 2nd term to the "x" term
            sum_third_num = first_num + second_num #increment
            first_num = second_num #for next iteration
            second_num = sum_third_num #for next iteration(it continues till the last term in the sequence)
        return second_num
    
x = int(input("Enter a positive number:")) #take the input
print(Fibonacci(x)) 

#Problem 5 Reverse the elements in the list
original_List = [] 

n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    pool_list = int(input()) #take elements in the list  
    original_List.append(pool_list) #append them to main list
    
print("The input list given by user",original_List)
#x = [int(x) for x in input("Input list: ").split(",")] whole thing can be repaced by one line
def reverse(original_List):
    new_List=original_List[::-1]  #using slicing method
    return new_List
print("The reversed list:",reverse(original_List))
print("The computational complexity for the above code is O(n)")

