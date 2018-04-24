import unittest
# -*- coding: utf-8 -*-
# CS 196 SP18 HW6
# This is a pretty short homework set.

def factorial(the_num):
    """
    Returns the factorial of a number. This is the product of all integers between 1 and the number, inclusive.

    Examples:
        Input:
            the_num = 5
        Output:
            120
            5 factorial (5!) = 5*4*3*2*1

    Args:
        (int) the_num: input number

    Returns:
        (int) the factorial of the_num
    """
    num = 1
    while the_num >= 1:
        num = num * the_num
        the_num = the_num - 1
    return num

def fibonacci(n):
    """
    Returns the nth fibonacci number.

    The Fibonacci arruence is defined recursively. The 0th and 1st Fibonacci numbers are 0 and 1,
    and the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers.

    Args:
        (int) n: Which fibonacci number to find

    Returns:
        (int) the nth Fibonacci number
    """
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def longest_increasing_subsequence(arr):
    """
    Given a list of numbers, returns the length of the longest increasing subsequence.

    A subsequence is an ordered but not necessarily contiguous part of an array.

    Examples:
        Input:
            [1,5,2,3]
        Output:
            3
            The longest increasing subsequence is [1,2,3].
            For this array:
            [1,5] is also an increasing subsequence.
            [1,2,3,5] is increasing, but not a subsequence.
            [5,3] is a subsequence, but not increasing.
            [3,2] is neither increasing nor a subsequence.

    Args:
        ([int]) arr: The input list

    Returns:
        (int) the length of the longest increasing subsequence

    """
    if not arr:
        return arr

    M = [None] * len(arr)    # offset by 1 (j -> j-1)
    P = [None] * len(arr)

    # Since we have at least one element in our list, we can start by
    # knowing that the there's at least an increasing subarruence of length one:
    # the first element.
    L = 1
    M[0] = 0

    # Looping over the arruence starting from the second element
    for i in range(1, len(arr)):
        # Binary search: we want the largest j <= L
        #  such that arr[M[j]] < arr[i] (default j = 0),
        #  hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if arr[M[upper-1]] < arr[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if arr[M[mid-1]] < arr[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    # this will also set the default value to 0

        P[i] = M[j-1]

        if j == L or arr[i] < arr[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [arr[M[L-1]], arr[P[M[L-1]]], arr[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(arr[pos])
        pos = P[pos]

    last = result[0]
    return last
