#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import operator

def print_words(filename):
	d = {}
	f = open(filename,'rU')
	text = f.read()
	splittedList = text.split()
	w=""
	for word in splittedList:
		w=w+" "+word.lower()
		if w in d:
			d[w]=d[w]+1
		else:
			d[w]=1
		w=word.lower()
	f.close()
	for k in sorted(d.keys()): print k , '  ' ,d[k]

def print_top(filename):
	d = {}
	f = open(filename,'rU')
	text = f.read()
	splittedList = text.split()
	w=""
	for word in splittedList:
		if "#" not in word: 
			w=w+" "+word.lower()
			if w in d:
				d[w]=d[w]+1
			else:
				d[w]=1
		w=word.lower()
	f.close()
	sortedList = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
	for i in range(50):
		print sortedList[i][0] , sortedList[i][1]

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
 	   print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
