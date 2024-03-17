import fun_generator as gn

def gn_shengke():
    """
        一个神奇的生成器,我自己标注的字典好像出了什么奇怪的问题,我不想再写一次,直接生成一下叭
    """
    ke = '金克木,木克土,土克水,水克火,火克金'
    sheng = '金生水,水生木,木生火,火生土,土生金'
    list = ['金','木','水','火','土']
    res = {}
    res = dict.fromkeys(list)
    for i in res:
        res[i] = dict.fromkeys(list,2)

    list = ke.split(',')
    for i in list:
        i = i.split('克')
        res[i[0]][i[1]] = -1
        res[i[1]][i[0]] = -2
    
    list = sheng.split(',')
    for i in list:
        i = i.split('生')
        res[i[0]][i[1]] = 0
        res[i[1]][i[0]] = 1
    print(res)
    return

if __name__ == '__main__':
    gn_shengke()