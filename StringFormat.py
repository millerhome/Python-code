#傳統寫法
print("Line1")
x=1+1
print("Line2")
first_name=input('Please input first name!')
last_name=input('Please input Last_name!')
print(first_name.capitalize() + ' ' + last_name.capitalize()) #capitalize將字串開頭轉大寫其它轉小寫

#output 字串物件 ,利用output物件,簡化print字串寫法,程式碼較簡潔
output='My name is '+first_name + last_name
print(output)
output='My name is {} {}'.format(first_name,last_name) #{}搭配 format語法..有順序性
print(output)
output='My name is {0}_{1}'.format(first_name,last_name)#{0}編號由0開始,有順序性
print(output)
output='My name is {1}_{0}'.format(first_name,last_name)#{0}編號由0開始,有順序性
print(output)
output=f'My name is {first_name} {last_name}' #此寫法僅支援python 3,f關鍵字表示format
print(output) 