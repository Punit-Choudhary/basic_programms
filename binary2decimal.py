#!python3
# binary2decimal.py - program to convert binary value to decimal
def bin2dec(binary):
	output = 0
	binary = list(binary)
	for i in range(len(binary)):
		output += (2 ** i) * int(binary.pop())
	print(f'decimal value {output}\n')

while True:
        value = input("Enter Binary value: ")
        if value == '':
                break
        else:
                try:
                        bin2dec(value)
                except:
                        print("Wrong Input !!\n")

