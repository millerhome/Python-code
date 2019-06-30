dict1={'name':'miller','age':30,'weight':60} #key-value的格式#
print(1,str(dict1['name'])) #指定Key以取得vale,此行加用str函數轉型輸出#
dict2=dict1.copy()  #copy()複製dict物件 dict1給dict2#
dict2.pop('name')  #pop()移除dict2的其中一個Key欄位'name'#
print(2,dict2)
dict2['name']='Nicole' #加回key欄位'name'並指定value為'Nicole'#
print(3,dict2)
dict2['name']='Jerry' #修改'name'的value為'Jerry'#
print(4,dict2)