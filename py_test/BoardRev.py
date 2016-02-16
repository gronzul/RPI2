#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  BoardRev.py

import sys
import wiringpi2 as p

def main(args):
	test1()
	return 0

def test1():
	print "#######################"
	print "Pi Board Revision: ", p.piBoardRev()
	print "#######################"
	return 0


if __name__ == '__main__':	
	sys.exit(main(sys.argv))
