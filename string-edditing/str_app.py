def converting_gramer(string):
    list1=string.split(' ')
    list2=[]
    list3=[]
    str1=''
    s=0
    for i in list1:
        if i=='the':
            list2.append(i.capitalize())
        elif i=='i' or i=='i,':
            list2.append(i.capitalize())
        elif i=='and' or i=='and,':
            list2.append(i.capitalize())
        else:
            list2.append(i)
    for i in list2:
        if s==1:
            list3.append(i.capitalize())
            s-=1
        elif i.endswith('.') or i.endswith(','):
            list3.append(i)
            s+=1
        elif i.startswith(',') or i.startswith(','):
            list3.append(i.capitalize())
        else:
            list3.append(i)
    list3.pop(0)
    list3.pop(0)
    
    x=list3[0]
    xx=x.capitalize()
    list3[0]=xx
    for i in list3:
        str1+=i+' '
    print(str1)

def number_commas(user_input):

    list1=user_input.split(' ')
    for i in list1:
        if i.isdigit():
            x=list1.index(i)
            s=f'{int(i):,d}' #this is just formula
            list1[x]=s
    str1 =' '
    for i in list1:
        str1+=' '
        str1+=i
    return(str1)


def sentence_word_finder(string,search_for_str):
    string1=string.lower()
    text=string1.split(' ')
    if search_for_str in text:
        find=text.index(search_for_str)
        if find == 0:
            print(search_for_str," is on first of the sentence")
        elif len(text)-find == 1:
            print(search_for_str,' is on last of the sentence')
        elif find <3 or len(text)-find<3:
            print("the sentence {} is after {} words here it's: \n".format(search_for_str,find+1)
                  +"{} '{}' {}".format(text[find-1],text[find],text[find+1]))
        elif find >=3:
            print("the sentence {} is after {} words here it's: \n".format(search_for_str,find+1)
                  +"{} {} {} '{}' {} {} {}".format(text[find-3],text[find-2],text[find-1],text[find],text[find+1],text[find+2],text[find+3]))
    else:
        print(search_for_str,"not is text")


def vowels_finder(string):
    vowels=["a","e","i","o","u"]
    vowels_found=[]
    string_lower=string.lower()
    for i in string_lower:
        if i in vowels:
            vowels_found.append(i)
        else:
            pass
    print("total a: ",vowels_found.count("a"))
    print("total e: ",vowels_found.count("e"))
    print("total i: ",vowels_found.count("i"))
    print("total o: ",vowels_found.count("o"))
    print("total u: ",vowels_found.count("u"))
    print("total vowels: ",len(vowels_found))

def count_currecters(string):
    upper_case=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    lower_case=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    number=['1','2','3','4','5','6','7','8','9']
    spacial_charecter=['!','@','#','$','%','^','&','*','(',')',',','-','_','+','=','{','}',']','[',':',':','<','>','.','?','/']
    upper_ans=[]
    lower_ans=[]
    number_ans=[]
    spacial_chr_ans=[]
    for i in string:
        if i in upper_case:
            upper_ans.append(i)
        elif i in lower_case:
            lower_ans.append(i)
        elif i in spacial_charecter:
            spacial_chr_ans.append(i)
        elif i in number:
            number_ans.append(i)
        else:
            pass
    print("total upper case: ",len(upper_ans))
    print("total lower case: ",len(lower_ans))
    print("total spacial charecter: ",len(spacial_chr_ans))
    print("total number: ",len(number_ans))

def upper_case_each(string):
    str1=''
    list1=string.split(' ')
    for i in list1:
        s=i.capitalize()
        str1+=s+' '
    return(str1)

def reversing_each(string):
    str1=''
    list1=string.split(' ')
    for i in list1:
        str1+=' '
        s=list(i)
        s.reverse()
        for i in s:
            str1+=i
    return(str1)

def white_space(string):
    str1=''
    str2=''
    for i in string:
        if i.isspace():
            str1+=i
        else:
            str2+=i
        
    return(str1+str2)

def reverse_string(string):
    list1=[]
    x= list(string.split(' '))
    while 0 != len(x):
        xx=x[-1]
        x.pop()
        list1.append(xx)
    str1=''
    for i in list1:
        str1+=' '
        str1+=i
    return(str1)

def dublicate_remove(string):
    ss=string.split(' ')
    list1=[]
    str1='' 
    xx=[]
    for i in ss:
        if i in ss:
            x=ss[ss.index(i)+1:len(ss)].count(i)
            if i not in xx:
                list1.append(i)
            if x>=1:
                xx.append(i)
    for i in list1:
        str1+=' '
        str1+=i
    return(str1)

def number_coding(string):
    #must only contain number and alphabate and ',' and '.'
    import random
    encoded_str=''
    coding2=['11','13','14','15','17','18','19','21','23','24','29','31','35','37','39','42','44','46','47','48','52','49','52','57','59','62','64','66','68','71','74','76','77','79','81','82','86','88','89','91','96','97','99']
    coding={' ':'53','q':'12','w':'45','e':'56','r':'34','t':'87','y':'65','u':'69','i':'55','o':'33','p':'63','a':'61','s':'85','d':'83','f':'58','g':'28','h':'25','j':'54','k':'72','l':'95','z':'51','x':'73','c':'93','v':'27','b':'92','n':'84','m':'26','1':'32','2':'43','3':'94','4':'41','5':'75','6':'78','7':'38','8':'67','9':'98','0':'22',',':'16','.':'36'}
    for i in string:
        if i in coding:
            encoded_str += coding[i]+'0'
        else:
            encoded_str += i+'0'
    list1=encoded_str.split('0')
    str1=''
    for i in list1:
        if i == '53':
            str1+= random.choice(coding2)+'0'
        else:
            str1+=i+'0'
    return(str1)

def number_decoding(number):
    coding2=['11','13','14','15','17','18','19','21','23','24','29','31','35','37','39','42','44','46','47','48','52','49','52','57','59','62','64','66','68','71','74','76','77','79','81','82','86','88','89','91','96','97','99']
    coding={' ':'53','q':'12','w':'45','e':'56','r':'34','t':'87','y':'65','u':'69','i':'55','o':'33','p':'63','a':'61','s':'85','d':'83','f':'58','g':'28','h':'25','j':'54','k':'72','l':'95','z':'51','x':'73','c':'93','v':'27','b':'92','n':'84','m':'26','1':'32','2':'43','3':'94','4':'41','5':'75','6':'78','7':'38','8':'67','9':'98','0':'22',',':'16','.':'36'}
    str1=[]
    decoded_str=''
    list1=number.split('0')
    for i in list1:
        if i in coding2:
            str1.append('53')
        else:
            str1.append(i)
    for i in str1:
        if i in coding.values():
            decoded_str += next(key for key,value in coding.items()if value==i)
        else:
            decoded_str += i
    return(decoded_str)




string=''
h=0
s=0
user_edited='hhhhhhj'
while True:
    
    print("welcome to the akki text_software")
    print("type 'end' to end this code")
    user_input=input("enter your sentence:  ")
    if user_input.isupper():
        user_input=user_input.lower()
    if user_input=='end' or user_input=='END':
        break
    print("\n\n")
    converting_gramer(number_commas(user_input))
    h=-h
    user_edited=str()

    while True:
        string= str()
        if h>=1:
            if user_edited=='':
                print("\n\n\n\n\n\nyou have't edited anything: \nhere is old str",user_input)
            else:
                print("\n\n\n\n\n\nyour edited text: \n",user_edited)
        if len(user_edited)<=1:
            string+=user_input
        else:
            string+=user_edited
            user_edited=''

        
        print("\nwhat you wanna do on your text: \n"
              +"...................................\n"
              +"a). do you wanna search something? type-'1' \n"
              +"b). do you wanna edit something? type-'2'\n"
              +"c). do you wanna code or decode? type-'3'\n"
              +"d). do you wanna end this code? type-'end'\n")
        user_ans=input("your choise........................... ")
        if user_ans == '1' or user_ans=='2' or user_ans=='3':
            h+=1
        if user_ans =='end' or user_ans=='END':
            print("your given str",user_input)
            print("your eddited str",user_edited,"\n\n\n\n\n\n")
            break
        match user_ans:
            case '1' :
                print("\n\n\n\n\nso you wanna search something....\n\n"
                      +"a). for search a word type '1'\n"
                      +"b). for count total vowels type '2'\n"
                      +"c). for count currecters type '3'\n")
                user_ans2=input("your response...............")
                if user_ans2=='1':
                    user_ans2_0 =input("type what you wanna find\n")
                    sentence_word_finder(user_input,user_ans2_0)
                    x=input("\nsimply tap 'enter' for continue")
                    

                if user_ans2=='2':
                    print("\n\n\n\nso you wanna calculate vowels....\n")
                    vowels_finder(user_input)
                    x=input("\nsimply tap 'enter' for continue")

                if user_ans2=='3':
                    print("\n\n\n\nso you wanna count currecters.....\n")
                    count_currecters(user_input)
                    x=input("\nsimply tap 'enter' for continue")
                
                
            case '2' :
                print("\n\n\n\n\nso you wanna edit your text.....\n\n"
                      +"a). convert each word to capitalize type '1'\n"
                      +"b). convert each word to reversed type '2'\n"
                      +"c). for move all white space to front type '3'\n"
                      +"d). for reverse the whole sentence type '4'\n"
                      +"e). for remove dublicate from sentence type '5'\n")
                user_ans3=input("your response........................")
                if user_ans3=='1':
                    print("\n\n\n\nso you wanna capitalize each...\n")
                    user_edited=upper_case_each(string)
                    print(user_edited)
                    x=input("\nsimply tap 'enter' for continue")
                if user_ans3=='2':
                    print("\n\n\n\nso you wanna reverse each word...\n")
                    user_edited=reversing_each(string)
                    print(user_edited)
                    x=input("\nsimply tap 'enter' for continue")
                if user_ans3=='3':
                    print("\n\n\n\nso you wanna white space to front...\n")
                    user_edited=white_space(string)
                    print(user_edited)
                    x=input("\nsimply tap 'enter' for continue")
                if user_ans3=='4':
                    print("\n\n\n\nso you wanna reverse the whole sentence...\n")
                    user_edited=reverse_string(string)
                    print(user_edited)
                    x=input("\nsimply tap 'enter' for continue")
                if user_ans3=='5':
                    print("\n\n\n\nso you wanna remove dublicate from sentence...\n")
                    user_edited=dublicate_remove(string)
                    print(user_edited)
                    x=input("\nsimply tap 'enter' for continue")
            case '3':
                print("\n\n\n\n\nso you wanna code or decode....\n\n"
                      +"a). for encoding the sentence type '1'\n"
                      +"b). for decoding the sentence type '2'\n")
                user_ans4=input("your response....................")
                if user_ans4=='1':
                    print("\n\n\n\nso you wanna encoding the sentence...\n")
                    user_edited=number_coding(string)
                    print(user_edited)
                    x=input("\nsimply tap 'enter' for continue")
                if user_ans4=='2':
                    print("\n\n\n\nso you wanna encoding the sentence...\n")
                    user_edited=number_decoding(string)
                    print(user_edited)
                    x=input("\nsimply tap 'enter' for continue")
                
                
                
            
                
                
                
                
                
            
            
            
            
                
        
    




