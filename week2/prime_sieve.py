from pylab import *



upper_bound = int(input("Input an upper bound for the prime number. "))
integer_list = [0] * upper_bound
stop_number = int(sqrt(upper_bound)) + 1
prime_list = []

for i in range (2, stop_number):
    if integer_list[i] != 1:
        integer_list[i] = i
        prime_list.append(i)
        print (i)
        for j in range(i*i, upper_bound, i):
            integer_list[j] = 1


for i in range (stop_number+1, upper_bound):
    if integer_list[i] !=  1:
        integer_list[i] = i
        prime_list.append(i)

print (prime_list[284])



