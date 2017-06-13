def is_rotation(s1,s2):
    if s1==None :return False
    if s1=='' and len(s2)!=0:return False
    if s1=='' and s2=='':return True
    if len(s1)!=len(s2):return False
    for i in range(len(s1)):
            if s1[i:] and s2[:i]:
                return True

print is_rotation('hello','lohel')
