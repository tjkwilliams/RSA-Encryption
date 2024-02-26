def mod(num1, num2):
	return num1 % num2



def decrypt(ciphertext):
	message = ""
	return message

# Message is an array of integers
def encrypt(message, e, n):


	ciphertext = ""

	for num in message:
		ciph = num ** e
		ciph2 = mod(ciph, n)
		ciphertext += ciph2

	return ciphertext

def main():
	
	calc = 43%492

	#heyllo

	print(calc)


if __name__ == '__main__':
	main()
