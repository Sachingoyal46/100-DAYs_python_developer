
def shift(arr,size):
    j=0
    for i in range(0,size-1):
        if(arr[i]<0):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j=j+1
    return arr        

arr=[-1,2,3,5,-3,-5,-7,9,8,4]
print(arr)
size=len(arr)
t=shift(arr,size)
print(t)