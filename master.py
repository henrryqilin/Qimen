from Modules.dipan import Di_Pan
from Modules.exit import exit

dipan = Di_Pan()
loop = exit()

support = {'1':dipan,'88':loop}

print('欢迎使用奇门遁甲小工具!\n请选择需要起的局')
print('1:地盘局 88:退出程序')

while True:
    x = input()
    if x in support:
        support[x].Run()
    else:
        print('不是哥们,咱真没那个能力,能看看上面写啥了吗.')
        continue