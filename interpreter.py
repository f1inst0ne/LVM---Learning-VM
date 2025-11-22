#Made by Pakhomov A.K. IKBO-17-22
import argparse

def mask(n):
    return ((2**n)-1)

def execute(bytecode):
	memory = [0] * 30

	for i in range(0, len(bytecode), 8):
		command = bytecode[i:i+8]
		command = int.from_bytes(command, 'little')
		op = command & 0B1111_11
		dest_addr = (command >> 6) & mask(13)
		if op == 59:
			value = (command >> 19) & mask(16)
			memory[dest_addr] = value
		if op == 40:
			source_addr = (command >> 19) & mask(13)
			memory[dest_addr] = memory[memory[source_addr]]
			
		if op == 56:
			source_addr = (command >> 19) & mask(13)
			memory[source_addr] = memory[dest_addr]
		if op == 34:
			source_addr = (command >> 19) & mask(13)
			memory[dest_addr] = -memory[source_addr]
	return memory
	
def main():
	#Arguments parse
	parser = argparse.ArgumentParser()        
	parser.add_argument('-i', '--input', required=True)      
	parser.add_argument('-o', '--output', required=True)
	args = parser.parse_args()



	with open(args.input, 'rb') as file:
		bytecode = file.read()

	print(execute(bytecode))

if __name__ == "__main__":
    main()