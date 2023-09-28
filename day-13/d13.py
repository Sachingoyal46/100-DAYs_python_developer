# def my_function():
#     for i in range(1,20):
#         if i==19:
#             print("you got it")

# my_function()            

# from random import randint

# dic_pic=["!","@","#","$","%","&"]
# dic_num=randint(0,5)
# print(dic_pic[dic_num])



def leap_year(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                print("leap year")
            else:
                print("not a leap year")
        else:
            print("leap year")

    else:
        print("not a leap year")

leap_year(2000)

