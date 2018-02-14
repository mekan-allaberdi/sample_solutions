import sys

roman_letter = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}

## 1. Rule of same or smaller values, put right to add.
## Values must be in non-increasing order
## 
## A part of rule 1
## Before I, cannot placed IV or IX 
## Before X, cannot placed XL or XC
## Before C, cannot placed CD or CM
## All three above has 4 or 9 times (1 -> 4,9) , (10 -> 40,90), (100 -> 500, 900)

## 2. Rule of three
rule_2 = {
	'I': 3,
	'V': 1,
	'X': 3,
	'L': 1,
	'C': 3,
	'D': 1,
	'M': sys.maxsize
}

## 3. Rule of subtract
rule_3 = {
	'IV': 4,
	'IX': 9,
	'XL': 40,
	'XC': 90,
	'CD': 400,
	'CM': 900
}


def int_val(letter):
	return roman_letter.get(letter, None)

def roman_to_int(str):

	int_res = 0  # converted result
	last_val = sys.maxsize  # last value
	curr_rep = 1  # repeat numbers of current value
	
	i=0
	n=len(str)
	str_list = list(str)
	
	while i<n:
		curr_val = roman_letter.get(str_list[i], None)
		if curr_val == None: # Invalid roman number
			return None

		# Proceed Rule 1
		if curr_val > last_val or last_val == curr_val*4 or last_val == curr_val*9:
			return None

		# Proceed Rule 2
		if curr_val == last_val:
			curr_rep += 1
			max_rep = rule_2[str_list[i]] # Am not checking dictionary, if it is not exist here, above I already checked it
			if curr_rep > max_rep:
				return None
		else:
			curr_rep = 1

		# Proceed Rule 3
		if i<n-1:
			rule2_val = rule_3.get(str_list[i]+str_list[i+1], None)
			if rule2_val:
				if rule2_val > last_val: # Ex : IIV
					return None 
				int_res += rule2_val
				i += 2
				last_val = rule2_val
				continue				

		i += 1
		int_res += curr_val
		last_val = curr_val

	return int_res

if __name__ == '__main__':
	str = input()
	result = roman_to_int(str)

	if result:
		print(result)
	else:
		print('INVALID NUMBER')


