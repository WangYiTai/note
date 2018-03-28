# encoding=UTF-8
loop=True
money=0
while loop:
    x = raw_input('提示：請投入金幣,結束投幣請按"q"鍵')
    if x=='q':
        if money==0:
            print '錯誤：您未投入過紙幣，請至少投入一張紙幣後才能選購商品'
        else:
            print '提示：您已結束投幣，將進入購買商品操作介面'
            loop = False
    else:
        try:
            x = int(x)
            money+=x
            print '提示：您此次投幣',x,'元人民幣，您一共投幣',money,'元人民幣'
        except Exception,e:
            print '錯誤：您的金幣系統不識別，請重新投幣，謝謝！'
 
GoodList = {
    '可口可樂':2.5,
    '果粒橙':3,
    '奶茶':1.5,
    '加多寶':4
}
 
i=0
print '請選擇商品：'
for x in GoodList:
    i+=1
    print '編號',i,'商品名稱',x,'價格',GoodList[x]
print
 
fanwei = range(len(GoodList))
loop = True
while loop:
    o = raw_input('提示：請輸入您要購買的商品編號，按"q"鍵結束購買')
    if o=='q':
        loop = False
    else:
        try:
            o = int(o)
            if o>=1 and o<=len(GoodList):
                i=0
                for x in GoodList:
                    i+=1
                    if i==o:
                        if money>=GoodList[x]:
                            money -= GoodList[x]
                            print '提示：您購買的商品是:',x,'，價格:',GoodList[x],'，您還剩餘：',money,'元人民幣'
                            if money==0:
                                loop = False
                        else:
                            print '錯誤：您的餘額',money,'元已不足購買此商品',x,'[',GoodList[x],'元]'
            else:
                print '錯誤：您輸入的商品編號不存在，請重新輸入'
        except Exception,e:
            print '錯誤：請輸入正確的產品編號，謝謝合作！'
 
if money>0:       
    print '提示：系統將找您，',money,'元人民幣，歡迎下次光臨'
else:
    print '提示：您的餘額已用完，歡迎下次光臨'
