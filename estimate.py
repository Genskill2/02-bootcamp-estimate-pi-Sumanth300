import random

def wallis():
	a=1000000
	product = 1
	n=1
	while (n<a):
		product = (product*4*n*n)/(4*n*n -1)
		n=n+1 		
	return (product*2)	
	
def monte_carlo():
	a=1000000
	square = 0
	circle = 0
	n=0
	for n in range(a):
		x=random.random()
		y=random.random()
		distance = (x*x)+(y*y)
		if (distance < 1):
			circle += 1
		square += 1
	pie = 4*(circle/square)
	return (pie)
wallis()
monte_carlo()
