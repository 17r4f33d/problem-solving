# Given a range (inclusive), find out the sum of all the even and odd fibonacci numbers in that range seperately.
# Can also be solved using the concept of perfect square.
# In that case, we can directly start from the starting point without having to calculate all the fibonacci numbers from 0 to starting point.
# That approach, however, does not improve the performance or execution time significantly.
from time import time
start = time()
def even_odd_fibonacci(start_inclusive, end_inclusive):
    prev_prev = 0
    prev = 1
    even_sum = 0
    odd_sum = 0
    count = 1
    while prev <= end_inclusive:
        if prev >= start_inclusive:
            if prev % 2 == 0:
                even_sum += prev
            else:
                odd_sum += prev
        nextt = prev_prev + prev
        prev_prev = prev
        prev = nextt
        count += 1
    return even_sum, odd_sum, count
print(even_odd_fibonacci(0, 10**18))
print("Took {taken_time} seconds".format(taken_time = time() - start))
