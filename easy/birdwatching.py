#!/usr/bin/python3
#
#Given a count of birds in a list and that each number relates to a different
#type of bird.  Return the id of the bird that occurs the most
#
#INPUT:
#8
#4 3 2 4 4 3 7 4
#
#OUTPUT:
#4

def migratorybirds(arr_count, arr):
    ordered=list(set(arr))
    iterator=0
    counts = []
    for item in ordered:
        itemcount=arr.count(item)
        iterator+=1
        counts.append(itemcount)
    high=max(counts)
    position=counts.index(high)
    return ordered[position]

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    result = migratorybirds(arr_count,arr)

    print(result)
