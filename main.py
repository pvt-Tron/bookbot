# !/usr/bin/python3
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
	# ls2 = len(sys.argv)
	# print(ls1)
	# print(ls2)
	# print(arg1s)
	la1 = len(arg1s)
	# print(la1)
	if la1 < 3:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)	
	arg2s = arg1s[2:] # # slice the 2 default agrs
	# print(arg2s)
	# for i in range(1, arg1s - 1):
	for arg2 in arg2s:
		inptpth = arg2
		
		# stpth1 = "~/wrksp/boot.dev/github.com/pvt-Tron/bookbot/"
		# print(stpth1)
		# inptpth = stpth1 + arg2
	 	# inptpth = sys.argv[i] ## <<<<<<

		# inptpth = "books/frankenstein.txt"
		# ## books/frankenstein.txt mobydick.txt prideandprejudice.txt

		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {inptpth}...") 
		print("----------- Word Count ----------")
		numwords = get_num_words(get_book_text(inptpth))
		# print(f"{numwords} words found in the document")
		print(f"Found {numwords} total words")
		print("--------- Character Count -------")
		cntchrdic = get_num_chars(get_book_text(inptpth))

		for i, j in cntchrdic.items():
			print(f"{i}: {j}")	
main()

