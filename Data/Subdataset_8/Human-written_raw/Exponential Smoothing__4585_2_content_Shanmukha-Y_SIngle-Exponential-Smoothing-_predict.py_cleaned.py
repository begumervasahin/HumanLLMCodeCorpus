import matplotlib.pyplot as plt
file=open("data.txt",'r')
data=list(map(float,file.read().strip().split("\n")))
k =[data[0], data[1]]
alpha=0.98
for i in range(2,len(data)):
    pre = alpha*data[i-1] + (1-alpha)*k[i-2]
    k.append(round(pre,3))
t=0
for i in range(len(data)):
    t=t+abs(data[i]-k[i])
t=t/len(data)
print(t)
plt.plot(data,color = "blue")
plt.plot(k,color="red")
plt.show()