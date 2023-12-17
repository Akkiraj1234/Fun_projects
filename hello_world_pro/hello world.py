import time
import os
import random

#normal version--------------------------------------------------------------------
# list1=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',',','.',"'",'"','<','>',')',':','(',';']
# x=input('enter the text you wanna print: ')
# text=''
# for i in x:
#     for s in list1:
#         if i==s:
#             text+=s
#             print(text)
#             time.sleep(0.026)
#             break
#         else:
#             print(text+s)
#             time.sleep(0.026)
# nothing=input()

#random normal version---------------------------------------------------------------
# list1=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',',','.',"'",'"','<','>',')',':','(',';']
# x=input('enter the text you wanna print: ')
# text=''
# for i in x:
#     while True:
#         s=random.choice(list1)
#         if i==s:
#             text+=s
#             print(text)
#             time.sleep(0.026)
#             break
#         else:
#             print(text+s)
#             time.sleep(0.026)
# nothing=input()

# advanced version with random
list1=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',',','.',"'",'"','<','>',')',':','(',';']
x=input('enter the text you wanna print: ')
text=''
for i in x:
    while True:
        s=random.choice(list1)
        if i==s:
            text+=s
            print(text)
            time.sleep(0.026)
            if text.strip()==x.strip():
                nothin=input()
            os.system('cls')
            break
        else:
            print(text+s)
            time.sleep(0.026)
            os.system('cls')
# thanks for using it tho akki :)