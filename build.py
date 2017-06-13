def is_rotation(s1,s2):
    if s1==None :return False
    if s1=='' and len(s2)!=0:return False
    if s1=='' and s2=='':return True
    if len(s1)!=len(s2):return False

    return(len(s1) == len(s2) and s1 in s2*2)

print is_rotation('hello','lohel')
