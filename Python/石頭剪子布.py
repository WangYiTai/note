# encoding=UTF-8
# 石頭剪子布 程式
# 李忠
import random
 
# 定義石頭剪子布字典
dict = {1:'剪子',2:'石頭',3:'布'}
 
for row in dict:
    print '編號:',row,' = ',dict[row]
 
print '您出什麼？'
 
loop = True
while loop:
    you = raw_input('請輸入編號回車: ')
    try:
        you = int(you)
        if you>=1 and you<=3:
            loop = False
        else:
            print '請輸入 1-3 範圍內的編號'
    except Exception,e:
        print '請輸入正確的數字編號'
 
dn = random.randint(1,3)
print '你出：',dict[you]
print '電腦出：',dict[dn]
print '結果：',
 
if dn==you:
    print '平局'
elif (you>dn and you-dn==1) or you+2==dn:
    print '你勝'
else:
    print '電腦勝'

