from Modules.dipan import Di_Pan
from Modules.exit import exit

dipan = Di_Pan()
loop = exit()

support = {'1':dipan,'88':loop}

print('欢迎使用奇门遁甲小工具!\n请选择需要起的局\n1:地盘局 88:退出程序')
x = input()

while True:
    if x in support:
        support[x].Run()
    else:
        print('不是哥们,咱真没那个能力,这玩意确实不会算.')
        print('欢迎使用奇门遁甲小工具!\n请选择需要起的局\n1:地盘局 88:退出程序')
        x = input()
        continue

    print('欢迎使用奇门遁甲小工具!\n请选择需要起的局\n1:地盘局 88:退出程序\n按Enter再开一盘')
    y = input()
    if y == '':
        pass
    else:
        x = y
    