
# 1st approch

# def similar(arr1,n,arr2,m):
#     i=0
#     j=0
#     arr1.sort()
#     arr2.sort()
#     unio=[]
#     inter=[]

#     while(i<n and j<m):
#         if(arr1[i]<arr2[j]):
#             unio.append(arr1[i])
#             i+=1

#         elif(arr1[i]>arr2[j]):
#             unio.append(arr2[j])
#             j+=1

#         else:
#             inter.append(arr1[i])
#             unio.append(arr1[i])
#             i+=1
#             j+=1   

#     while(i<n):
#         unio.append(arr1[i])
#         i+=1

#     while(j<m):
#         unio.append(arr2[j])
#         j+=1    

#     return len(inter),len(unio)

#2nd approch

def similar(arr1,n,arr2,m):
    set1=set(arr1)
    set2=set(arr2)

    union=list(set1 | set2)
    intersection=list(set1 & set2)

    return len(union),len(intersection)


arr1=[1,2,3,4,5]
n=len(arr1)

arr2=[4,6,2]
m=len(arr2)

a,b=similar(arr1,n,arr2,m)
print(a,b)