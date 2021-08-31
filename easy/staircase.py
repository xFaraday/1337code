#!/bin/python3
#
#Given a number, make a staircase that size
#
#INPUT:
#6
#
#OUTPUT:
#       #
#      ##
#     ###
#    ####
#   #####
#  ######

n = int(input())
loop = n + 1
counter = n
i = 0


while i < loop:
    print(' '*counter + '#'*i)
    i += 1
    counter -= 1





