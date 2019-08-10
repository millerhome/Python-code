#本範例會用list、if及wheil技巧，以傳入list及目標參數，找出list中，最接近目標參數的值
def fun1(list,ss) :
    max=len(list)
    i=1
    rult=ss
    while i<max:
        if list[i]>ss:
            print('%s %d'%(list[i],rult)) #print多參數
            if list[i] >rult or list[i]>ss:
               if rult>ss and rult<list[i]:
                    rult=rult
               else :
                    rult=list[i]
            i+=1
        else:
            i+=1
    return rult
litAA=[0,5,2,4,6,7,8,10]
AA=str(fun1(litAA,3))
print('找出list中，最接近目標參數的值:'+AA) 