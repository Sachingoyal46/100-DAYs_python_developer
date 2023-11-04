# def maxmin(arr):
#     arr.sort()
#     dic={"max":arr[0],"min":arr[-1]}
#     return dic


# arr=[100,2,30,4,5,6,7,8,9]
# t=maxmin(arr)
# print("maximum elements is",t["max"])
# print("minimum element is ",t["min"])

# using liner approach

# def maxmin(arr,size):
#     max=0
#     min=0
#     if(size==1):
#         max=arr[0]
#         min=arr[1]
#     if(arr[0]>arr[1]):
#         max=arr[0]
#         min=arr[1]

#     else:
#         min=arr[0]
#         max=arr[1]     

#     for i in range(2,size):
#         if(arr[i]<min):
#             min=arr[i]
#         elif(arr[i]>max):
#             max=arr[i] 

#     print(min)
#     print(max)                









arr=[100,20,40,29,1,5,23]
size=len(arr)
maxmin(arr,size)
