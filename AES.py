#Jack Amos
#Hw 3
#AES
#Python 3.7

key="0f1571c947d9e8591cb7add6af7f6798"

#operations
def SubBytes(block):
	pass




def ShiftRows(block):
	pass




def MixColumns(block):
	pass




def AddRoundKey(block):
	pass





#Get input
plaintext = input("Enter a string: ")

n = 16

#string made to be correct size for processing
if len(plaintext)%16 != 0:
	while n < len(plaintext):
		n+=16

	diff = n - len(plaintext)
	while diff != 0:
		plaintext+="0"
		diff-=1


#divide plaintext into blocks
blocks = []
b_start = 0
b_end = 15
temp = ""

while b_start < len(plaintext)-1:
	temp = plaintext[b_start:b_end]
	blocks.append(temp)


#encryption
rounds = 0

for n in blocks:
	while rounds < 11:
		if rounds == 0:
			AddRoundKey(n)
		elif rounds == 10:
			SubBytes(n)
			ShiftRows(n)
			AddRoundKey(n)
		else:
			SubBytes(n)
			ShiftRows(n)
			MixColumns(n)
			AddRoundKey(n)
		rounds+=1
	rounds = 0








