def Hello(who,SayWorld) :  #定義有多個引數的函式
    print(who+' '+ SayWorld) #用縮排判斷function內需執行程式碼
    print('2 '+who+' '+SayWorld)

def Hello2(who,SaySomething) :
        sayword=who+SaySomething
        return ('hello2無言'+' '+sayword,'回傳成功') #函數回傳多個值

Hello('miller','hihi') #呼叫函數1
s1,s2=Hello2('jerry','HAHA') #呼叫函數2 接一個以上的回傳值
print(s1,s2)