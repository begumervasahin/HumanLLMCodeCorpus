n=int(input("Input the range number: "))
perfect_number=2
while perfect_number<n :
	sum=0
	b=1
	while b<perfect_number :
		if perfect_number%b==0 :
			sum=sum+b
			b=b+1
		else :
			b=b+1
	if sum==perfect_number :
		print(perfect_number)
	perfect_number+=1