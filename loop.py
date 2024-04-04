## Loop
# nums = (22,33,32,4,5,67,88,99,122,44)
# find = 33
# count = 0
# while count <= len(nums):
#   if(nums[count] == find):
#     print("i fuund this", nums[count] )
#     break
#   else: 
#     print("finding..")
#   count += 1


i = 0
while i <= 10:
  if(i % 2 == 0):
    i+=1
    continue
  print("even", i)
  i+=1
  
  values = ["gowtam", "paul"]
  
  for elem in values:
    print("elemmtn", elem)

  else: 
    print("End")