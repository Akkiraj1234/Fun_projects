string="hi i am akki and akki has, hi hi i am lol. yaadav and i am akki 2000000000"
number="2505503705504206102603106107207205502306108408303506107207205503702506108501601902505505202505501705504206102604209503309503607106506106108306102707406108408304605508906102606806107207205502304302202202202202202202202202200"
#print(ss,"\n")
#for i in ss:
 #   if i in ss:
 #       ss.remove(i)
#print(ss,"\n")
#print(list1)


def white_space(string):
    str1=''
    str2=''
    for i in string:
        if i.isspace():
            str1+=i
        else:
            str2+=i
        
    print(str1+str2)


def reversing_each(string):
    str1=''
    list1=string.split(' ')
    for i in list1:
        str1+=' '
        s=list(i)
        s.reverse()
        for i in s:
            str1+=i
    print(str1)

def sentence_word_finder(string,search_for_str):
    text=string.split(' ')
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
        print(search_for_str," not in the given list")



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




def upper_case_each(string):
    str1=''
    list1=string.split(' ')
    for i in list1:
        s=i.capitalize()
        str1+=s+' '
    print(str1)
    
def converting_gramer(string):
    list1=string.split(' ')
    list2=[]
    list3=[]
    str1=''
    s=0
    for i in list1:
        if i=='the':
            list2.append(i.capitalize())
        elif i=='i':
            list2.append(i.capitalize())
        elif i=='and':
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
        else:
            list3.append(i)
    for i in list3:
        str1+=i+' '
    print(str1)

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
            
        

def password_checker(password):
    pass

def password_checker(string):
    print("its on under devlopment")
    pass


def most_used_sentence(string):
    pass

