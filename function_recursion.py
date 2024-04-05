# function and recursion
# newInput = int(input("Enter your number"))

# if(int(newInput)): 
#   print("this input is valid number")
# else: 
#    print('this input is not number')

# def sumFun(a):
#   sum = 0
#   while sum <= a:
#       sum += 1
#       print(sum)
#   return sum

# print(sumFun(newInput))


# recursion
# def recursion_fun(n):
#   if(n ==0):
#     return
#   print(n)
#   recursion_fun(n-1)

# recursion_fun(10)

# question: 
  # write a recursive function to calculate the sum of first na natural numbers
  # ans:
# getInput = int(input("enter your number"))

# def factorial_fun(n):
#   if(n == 0 or n==1):
#     return 1
#   print(n)
#   return n + factorial_fun(n-1)

# print(factorial_fun(getInput))

# question a recursive function to print all element in a list
rlist = ['mango', 'orange', 'bedana', 'tok']

def print_all_by_recursion(list, idx=0):
  if(idx == len(list)):
    return
  print(list[idx])
  return print_all_by_recursion(list, idx+1)

print_all_by_recursion(rlist, 0)