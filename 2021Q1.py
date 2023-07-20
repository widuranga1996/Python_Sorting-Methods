# Q1
# A

#print(max(2,3,5))

# #B
# number= int(input("Enter any number :"))
# temp=number
# #calculate reverse of this number
# reverse_num=0
# i=0
# # while i in range(0,4):
# while(number>0):
#     #extract last digit of this number
#     digit=number%10
#     # print("digit :",digit)
#     #append this digit in reverse number
#     reverse_num=reverse_num*10+digit
#     # print("reverse_num :",reverse_num)
#     #floor divide the number leave out the last digit from number
#     number=number//10
#     # print("number : ",number)
#     # i=i+1
    
# #compare reverse to orginal number
# if(temp==reverse_num):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")


# #C

# x1=5
# y1=5
# x2="UCSC"
# y2="UCSC"
# x3=[1,2,3]
# y3=[2,3,4]
# print(x1 is not y1)
# print(x2 is y2)
# print(x3 is y3)
# x3={1,2,3}
# y3={2,3,4}
# print(x3-y3)

# #Answer
# False
# True
# False
# {1}

# #D
# x=int(input("Enter number x:"))
# n=int(input("Enter number n:"))

# def fact(h):  
#     if(h==0):
#         return 1
#     else:
#         # print("dd",x)
#         fact1 = 1
        
#         for i in range(1,h+1):
#             fact1=fact1*i
#         return fact1
        
# # fact(x)
# # list=[1]
# j=1
# for i in range(1, n+1):
    
#     k = (x**i)/fact(i)
#     # list.append(k)
#     j+=k
# # print(sum(list))
# print(j)

# #E

# t=0
# sum=0
# for i in range(0,3):
#     print("i in 1st loop",i)
#     for j in range(3,5):
#         print("i",i)
#         print("j",j)
#         print("Before t",t)
#         t+=i-j*3
#         print("After t",t)
#         sum=sum+t
# print(t**2)

# #Answer: 3249

##F

#   Best case: worst case:
# i. o(1)         o(n)
# ii.o(n)         o(n)
# iii.o(n)        o(n)
# iv.o(n)         o(n^2)




    
