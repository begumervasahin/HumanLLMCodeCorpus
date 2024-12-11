from math import sqrt;
lambda testdata:sorted(map(lambda x:distance(testdata,x),dataSet))
lambda a,b:sqrt(
    (lambda x,y:x+y)
    (pow((lambda x,y:abs(x-y))(a[0],b[0]),2.0),
     pow((lambda x,y:abs(x-y))(a[1],b[1]),2.0))
    )
((lambda distance:map(lambda x:distance([1.0,1.1],x),
                     [[1.0,1.1],
                     [1.0,1.0],
                     [0.0,0.0],
                     [0.0,0.1]]))
(lambda a,b:sqrt(
    (lambda x,y:x+y)
    (pow((lambda x,y:abs(x-y))(a[0],b[0]),2.0),
     pow((lambda x,y:abs(x-y))(a[1],b[1]),2.0))
    ))
 )
import time
from math import sqrt
b1 = time.clock()
b2 = [[1.0,1.1],
         [1.0,1.0],
         [0.0,0.0],
         [0.0,0.1]]
b3 = ['A','A','B','B']
b4 = [1.0,1.1]
b5 = (lambda testdata,dataSet,label,k:
    (lambda x:x[0][x[1].index(max(x[1]))])
    ((lambda x:[x,map(x.count,x)])
    (map(lambda x:label[x],
    (lambda x:map(x[0].index,x[1][0:k]))
    (
        (lambda lst:[lst,sorted(lst)])
        ((lambda distance:map(lambda x:distance(testdata,x),dataSet))
            (lambda a,b:sqrt((lambda x,y:x+y)
            (pow((lambda x,y:abs(x-y))(a[0],b[0]),2.0),
             pow((lambda x,y:abs(x-y))(a[1],b[1]),2.0))
            ))
        )
    )
         ))
     )
 )(b4,b2,b3,3)
print "%f,%s"%(time.clock()-b1,b5)
print (lambda testdata,dataSet,label,k:(lambda x:x[0][x[1].index(max(x[1]))])((lambda x:[x,map(x.count,x)])(map(lambda x:label[x],(lambda x:map(x[0].index,x[1][0:k]))((lambda lst:[lst,sorted(lst)])((lambda distance:map(lambda x:distance(testdata,x),dataSet))(lambda a,b:sqrt((lambda x,y:x+y)(pow((lambda x,y:abs(x-y))(a[0],b[0]),2.0),pow((lambda x,y:abs(x-y))(a[1],b[1]),2.0))))))))))([1.0,1.1],[[1.0,1.1],[1.0,1.0],[0.0,0.0],[0.0,0.1]],['A','A','B','B'],3)