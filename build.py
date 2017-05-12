#Determine if a string is a rotation of another

def is_rotation(str1, str2):
    if(len(str1) == len(str2) and str1 in str2*2):
        return True
       # print("str1 is a rotation of str2")
    else:
        return False
        #print("str1 is not a rotation of str2")

value = is_rotation("sye","yes")
print(value)
