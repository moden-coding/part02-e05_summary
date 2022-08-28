#!/usr/bin/env python3

import math
import sys

def summary(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            if line:
                try:
                    x = float(line)
                    numbers.append(x)
                except ValueError:
                    print("Not a number!")
                    
    
    sum_nums = sum(numbers)
    average = sum_nums/len(numbers)

    return (sum_nums,average,get_stdev(numbers, average))

def get_stdev(L, calc_average):
    quotient_sum = 0
    for i in L:
        quotient_sum += (i-calc_average)**2
    return math.sqrt((quotient_sum)/(len(L)-1))

def main():

    files = sys.argv[1:]
    for i in files:
        data = summary(i)
        print(f"File: {i} Sum: {data[0]:.6f} Average: {data[1]:.6f} Stddev: {data[2]:.6f}")

if __name__ == "__main__":
    main()
