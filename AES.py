#Jack Amos
#Hw 3
#AES
#Python 3.7

#operations
def SubBytes(block):
	
	#untransformed s_box, 16x16
	s_box = list(range(256))

	return block


def shift(row,shift_no):

	temp = ""

	row_lst = list(row)

	#performs circular left shift
	while shift_no != 0:
		temp = row_lst[3]
		row_lst[3] = row_lst[0]
		row_lst[0] = row_lst[1]
		row_lst[1] = row_lst[2]
		row_lst[2] = temp
		shift_no-=1
	
	row = row_lst[0] + row_lst[1] + row_lst[2] + row_lst[3]

	return row


def ShiftRows(block):
	
	row1 = block[0:4]
	row2 = block[4:8]
	row3 = block[8:12]
	row4 = block[12:16]
	
	row1 = shift(row1,0)
	row2 = shift(row2,1)
	row3 = shift(row3,2)
	row4 = shift(row4,3)
	
	block = row1 + row2 + row3 + row4

	return block



def MixColumns(block):
	
	mix_matrix = [2,3,1,1,1,2,3,1,1,1,2,3,3,1,1,2]
	block_lst = list(block)

	col1 = []
	col2 = []
	col3 = []
	col4 = []
	col_count = 4
	i = 0

	while col_count != 0:
		col1.append(block_lst[i])
		col2.append(block_lst[i+1])
		col3.append(block_lst[i+2])
		col4.append(block_lst[i+3])
		i+=4
		col_count-=1

	#mm x col1(4x1 column)
	



	return block




def AddRoundKey(block):
	
	key="0f1571c947d9e8591cb7add6af7f6798"



	return block





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
b_end = 16
temp = ""
ciphertext = ""

while b_start < len(plaintext)-1:
	temp = plaintext[b_start:b_end]
	blocks.append(temp)
	b_start+=16
	b_end+=16


#encryption
rounds = 0

for n in blocks:
	while rounds < 11:
		if rounds == 0:
			arkr = AddRoundKey(n)
		elif rounds == 10:
			sbr = SubBytes(n)
			srr = ShiftRows(sbr)
			arkr = AddRoundKey(srr)
		else:
			sbr = SubBytes(n)
			srr = ShiftRows(sbr)
			mcr = MixColumns(srr)
			arkr = AddRoundKey(mcr)
		rounds+=1
	rounds = 0
	ciphertext+=arkr

print(ciphertext)





