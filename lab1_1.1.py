import time
import matplotlib.pyplot as plt

def iterative_sum(N):
    sum_ = 0
    for i in range(1, N+1):
        sum_ += i
    return sum_

def recursive_sum(N):
    if N == 0:
        return 0
    else:
        return N + recursive_sum(N-1)

def measure_time(func, N):
    start_time = time.time()
    func(N)
    end_time = time.time()
    return end_time - start_time

N_values = list(range(1, 1001, 50))

iterative_times = []
recursive_times = []

for N in N_values:
    iterative_times.append(measure_time(iterative_sum, N))
    recursive_times.append(measure_time(recursive_sum, N))

plt.plot(N_values, iterative_times, label='Iterative')
plt.plot(N_values, recursive_times, label='Recursive')
plt.xlabel('Value of N')
plt.ylabel('Time taken (seconds)')
plt.title('Time taken to compute sum of first N natural numbers')
plt.legend()
plt.show()
