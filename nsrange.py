#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Script that solves a range of IP in the name of a file
# File name: nsrange.py
# Author : Simone Dellabora
# Version 0.01

# import module
import sys
import time
import socket
import ipaddress

def main():

  f = sys.argv[1]

  # open file passend as argument
  RANGEIP = open(f, 'r')

  RANGEIP.readline()

  for ip in RANGEIP:
    try:
      list=socket.gethostbyaddr(ip)
      time.sleep(1)
      print(list)
    except IOError:
      pass

  RANGEIP.close()

  print ("end nslookup")

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
