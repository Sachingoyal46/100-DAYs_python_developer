

# iterative approach 

# def reverse(list,size):
#     start=0
#     last=size-1
#     while(start<last):
#         list[start],list[last]=list[last],list[start]
#         start+=1
#         last-=1



# list=[1,2,3,4,5,6,7,8]
# print(list)
# size=len(list)
# reverse(list,size)
# for i in range(size):
#     print(list[i],end=' ')

#recursive appraoch

def reverse(list , t , size):
    start=t
    last=size
    if(start>=last):
        return
    list[start],list[last]=list[last],list[start]
    reverse(list,start+1,last-1)


   
    


list=[1,2,3,4,5,6,7,8]
print(list)
size=len(list)-1
reverse(list,0,size)
print(list)