#!/usr/bin/python3
#
#Program counts the number of tallest "candles" in a list
#Input:
#4
#3 1 2 3
#
#Output:
#2
#

def birthdayCakeCandles(candles):
    candles.sort(reverse=True)
    candlescount = candles.count(candles[0])
    return candlescount

if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)
