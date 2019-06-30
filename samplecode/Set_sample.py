smp1=set(['張飛','關羽','劉備','趙雲'])
print(smp1)
smp1.add('馬超') #新增'馬超'至smp1
print("新增'馬超'至smp1:" , smp1)
smp2=smp1.copy() #複製相同set object#
print("複製相同set object:",smp2)
smp2.remove('馬超')
print("移除set中的陣列:",smp2)
#----------------------------------
#判斷某值是否存在set物件中#
print(smp1)
print('馬超' in smp1)
print(smp2)
print('馬超' in smp2)
#------------------------------------
print(smp1.intersection(smp2)) #smp1跟smp2的交集#
print(smp1.union(smp2)) #smp1與smp2的聯集
print(smp1.difference(smp2))#smp1與smp2的差集,只存在smp1的值# 