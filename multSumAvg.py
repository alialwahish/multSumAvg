for i in range(0,1000):
    if i%2!=0:
        print i,
print("")
'''looping up to the last number getting the range and adding the condition 
%2!=0 to check every pass for the odd numbers only then printing the current number (i)'''


i=5
n=0
while n<1000000:
    n=i*5
    i+=1
    print(n)

''' applying the same method only this time we;re modding by 5 i%5==0 get the ones that are mod 5 = 0'''
a = [1, 2, 5, 10, 255, 3]
sLi=0
for s in a:
    sLi+=s
print "sum of array: ",sLi
print "average of array: ",sLi/len(a)


