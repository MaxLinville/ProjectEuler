'''#largest prime factor
num = 600851475143
greatest_factor = 0

def main():
	for i in range(int(num**(1/2))):
		index = i+1
		if is_factor(index, num):
			if int(num/index) >= index and is_prime(int(num/index)):
				if int(num/index) > greatest_factor: 
					greatest_factor = int(num/index)
			elif is_prime(index):
				greatest_factor = index
	print(greatest_factor)
'''
def is_factor(divisor,num):
	if num % divisor == 0:
		return True
	return False

def is_prime(n):
	for i in range(int(n**(1/2))+1):
		if is_factor((i+1),n) and not(i+1 == 1):
			return False
	return True


#Largest palindrome product
'''def main():
	array = []
	maximum = 0
	for i in range(1000):
		for j in range(1000):
			product = i*j
			product_string = str(product)
			if is_palindrome(product_string):
				array.append(product)
	for n in range(len(array)):
		if array[n] > maximum:
			maximum = array[n]
	print(maximum)
'''
def is_palindrome(n):
	for l in range(int(len(n)/2)):
		if n[l] != n[-1*l-1]:
			return False
	return True

#Smallest multiple
'''def main():
	x = False
	i = 200000000
	num = 20
	count = 0
	while(x == False):
		for j in range(1, num+1):
			if (i%(j) == 0):
				count += 1
		if (count == num):
			x = True
			print(i)
		if (i%1000000 == 0):
			print(i)
		count = 0
		i += 1'''

#Sum square difference
'''def main():
	num = 100
	sum_squares = 0
	squared_sum = 0
	running_sum = 0
	for i in range(num):
		sum_squares += (1+i)**2
		running_sum += i+1
	squared_sum = running_sum**2
	print(squared_sum-sum_squares)'''

#10001st prime
'''def main():
	prime = 1
	index = 2
	while prime < 10001:
		if is_prime(index):
			prime+=1
		index+=1
	print(index-1)
'''

#largest paroduct in series
'''def main():
	max_val = 0
	num = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
	for i in range(len(num)-13):
		product = 1
		for j in range(13):
			product = product*int(num[i+j])
		if product > max_val:
			max_val = product
	print(max_val)'''

#Special Pythagorean Triplet
'''def main():
	x=True
	while(x==True):
		for i in range(1,1000):
			a=i
			for j in range(1,1000):
				b=j
				c=(a**2 + b**2)**(1/2)
				if (int(c) == c and a+b+c == 1000):
					print(a*b*c)
					x=False'''

#Summation  of primes
'''def main():
	prime_list = []
	for i in range(2,2000000):
		if is_prime(i):
			prime_list.append(i)
	print(sum_list(prime_list)+2)'''

def sum_list(n):
	total = 0
	for i in range(len(n)):
		total += n[i]
		print(n[i])
	return total

#Largest Product in a Grid

#Divisibility of Harmonic Number Denominators - this is way too hard
'''def main():
	M = 3
	highest = 0
	H = harmonic_number(243903723551)
	print(H)
	print(highest)'''

def harmonic_number(n):
	num = 1
	denom = 1
	for i in range(1,n):
		num = ((i+1)*num+denom) #Fraction addition
		denom = (denom*(i+1))
		common = gcd(num,denom)
		num = num//common
		denom = denom//common
	return num, denom


def gcd(x, y): #Euclidian algorithm
	while(y):
		x, y = y, x%y

	return x

if __name__ == "__main__":
	main()