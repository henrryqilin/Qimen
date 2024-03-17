# speed for generator is not necessary
# because it run only once

def dict_output(Key_List,Value_List):
    if len(Key_List) != len(Value_List):
        print('不是哥们,你这左右腿不一般长我咋整啊.')
        assert 9 > 10

    with open('output.txt','w',encoding='utf-8') as f:
        f.write('{')
        for i in range(len(Key_List)):
            f.write('\'{0}\':\'{1}\','.format(Key_List[i],Value_List[i]))

        f.seek(f.tell() - 1)
        f.write('}')
    return

def list_output(List):
    with open('output.txt','w',encoding='utf-8') as f:
        f.write('[')
        for i in range(len(List)):
            f.write('\'{0}\','.format(List[i]))

        f.seek(f.tell() - 1)
        f.write(']')
    return

def ganzhi_conjugate(Lista,Listb,Mode = 'merge',Path = 'output.txt'):
    """
        Mode = 'merge','part','output
    """
    len_a,len_b = len(Lista),len(Listb)
    
    count_process = [len_a,len_b]
    while True:
        if count_process[0] % count_process[1] != 0:
            c = count_process[0]
            count_process[0] = count_process[1]
            count_process[1] = c % count_process[0]
        else:
            hcf = count_process[1]
            break
    
    lcm = int(len_a * len_b / hcf)

    list1 = []
    list2 = []
    for i in range(int(lcm / len_a)):
        for line in Lista:
            list1.append(line)

    for i in range(int(lcm / len_b)):
        for line in Listb:
            list2.append(line)
    
    if Mode == 'merge':
        res = []
        for i in range(lcm):
            res.append(str(list1[i]) + str(list2[i]))
        return res
        
    elif Mode == 'part':
        return list1,list2
    elif Mode == 'output':
        with open(f'{Path}','w',encoding = 'utf-8') as f:
                    f.write('[')
                    for i in range(lcm):
                        f.write('\'{0}{1}\','.format(list1[i],list2[i]))

                    f.seek(f.tell() - 1)
                    f.write(']')

def list_repet_generator(Repet_List,Times):
    """
        [1,2,3,1,2,3]
    """
    res = []
    for line in range(Times):
        for i in Repet_List:
            res.append(i)
    
    return res

def repet_element_generator(Repet_List,Times):
    """
        [1,1,1,2,2,2,3,3,3]
    """
    res = []
    for i in Repet_List:
        for line in range(Times):
            res.append(i)
    
    return res

def file2py(File_Name,Open_Mode = 'r',Encoding = 'utf-8'):
    with open(File_Name,mode = Open_Mode,encoding = Encoding) as f:
        return eval(f.read())


if __name__ == '__main__':
    dict_output(list(range(1,13)),list('木木土火火土金金土水水土'))