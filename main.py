#!/usr/bin/python3
import sys
from stats import get_num_words
from stats import get_num_chars
from stats import prnt_lst

def get_book_text(inpt):
	with open(inpt) as f:
		filecontent = f.read()
#	return get_num_words(filecontent)
	return filecontent

def main():
	# sys.argv[1] = "books/"
	arg1s = sys.orig_argv
	# ls1 = len(sys.orig_argv)
	ls1 = len(sys.argv)
	# print(ls1)
	# print(arg1s)
		
	# arg2s = arg1s[2:]
	i2 = 1
	for i in range(1, ls1):
		i2 += 1
		# if(i < 2):
		# 	continue
		inptpth = sys.argv[i]
	if i < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
		# inptpth = "books/frankenstein.txt"
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {inptpth}...") # books/frankenstein.txt
		print("----------- Word Count ----------")
		numwords = get_num_words(get_book_text(inptpth))
		# print(f"{numwords} words found in the document")
		print(f"Found {numwords} total words")
		print("--------- Character Count -------")
		cntchrdic = get_num_chars(get_book_text(inptpth))
		# print(cntchrdic)
		# print(repr(cntchrdic))
		flag1 = 1
		for i, j in cntchrdic.items():
			# if flag1 == 1:
			# 	flag1  = 0
			# 	continue
			# else:
			print(f"{i}: {j}")

		# prnt_lst(cntchrdic)
	
main()

