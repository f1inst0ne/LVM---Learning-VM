#Made by Pakhomov A.K. IKBO-17-22
import argparse
import yaml
from pprint import pprint

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



#ASM operations
def write_const(dest_addr: int, value: int):
	result = 0
	result |= 59
	result |= (dest_addr << 6)
	result |= (value << 19)
	return result.to_bytes(8, 'little')

def read(dest_addr: int, source_addr: int):
	result = 0
	result |= 40
	result |= (dest_addr << 6)
	result |= (source_addr << 19)
	return result.to_bytes(8, 'little')

def write_value(dest_addr: int, value: int):
	result = 0
	result |= 56
	result |= (dest_addr << 6)
	result |= (value << 19)
	return result.to_bytes(8, 'little')

def un_sub(dest_addr: int, source_addr: int):
	result = 0
	result |= 34
	result |= (dest_addr << 6)
	result |= (source_addr << 19)
	return result.to_bytes(8, 'little')

# Given ASM tests
def test():
	assert list(write_const(423, 576)) == [0xFB, 0x69, 0x00, 0x12, 0x00, 0x00, 0x00, 0x00], 'ASM ERROR: WRITE_CONST FUNC '
	assert list(read(554, 123)) == [0xA8, 0x8A, 0xD8, 0x03, 0x00, 0x00, 0x00, 0x00], 'ASM ERROR: READ FUNC'
	assert list(write_value(682, 602)) == [0xB8, 0xAA, 0xD0, 0x12, 0x00, 0x00, 0x00, 0x00], 'ASM ERROR: WRITE_VALUE FUNC'
	assert list(un_sub(995, 87)) == [0xE2, 0xF8, 0xB8, 0x02, 0x00, 0x00, 0x00, 0x00], 'ASM ERROR: UN_SB FUNC'
	print('ASM FUNC TESTS: PASSED')

def asm(text):
	bytecode = bytes()

	for i in text.get('commands'):
		op = list(i.keys())[0]
		op_args = list(i.values())[1:]
		if op == 'write_const':
			bytecode += write_const(*op_args)
		elif op == 'read':
			bytecode += read(*op_args)
		elif op == 'write_values':
			bytecode += write_value(*op_args)
		elif op == 'un_sub':
			bytecode += un_sub(*op_args)
		else:
			print('OP ERROR')
	return bytecode

def main():
	#Arguments parser
	parser = argparse.ArgumentParser()        
	parser.add_argument('-i', '--input', required=True)      
	parser.add_argument('-o', '--output', required=True)
	parser.add_argument('-t', '--test', required=True)
	args = parser.parse_args()

	#Reading data from file
	with open(args.input, 'r') as file:
		input_text = yaml.load(file, Loader)


	bytecode = asm(input_text)

	#Making bin
	with open(args.output, 'wb') as output_file:
		output_file.write(bytecode)


	#Test mode
	if args.test == '1':
		test() 
		print('USED ARGUMENTS: -i %s -o %s -t %s' % (args.input, args.output, args.test))
		print('DATA FROM FILE:',)
		pprint(input_text)
		print('BYTECODE:')
		print(*[hex(i) for i in bytecode])
		print('BYTES COUNT:', len(bytecode))

if __name__ == "__main__":
    main()