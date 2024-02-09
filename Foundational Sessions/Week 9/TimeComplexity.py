import time
import matplotlib.pyplot as plt

input_size = []
plus_results = []
join_results = []


for i in range(100, 500000, 100):
    input_size.append(i)
    print(i)
    # String Concatenation using '+'
    start_time = time.time()
    concat_str = ""
    for _ in range(i):
        concat_str += "hello "
    end_time = time.time()
    plus_results.append(end_time-start_time)

    # String Concatenation using 'join()'
    start_time = time.time()
    join_str = ''.join(["hello " for _ in range(i)])
    end_time = time.time()
    join_results.append(end_time-start_time)


plt.plot(input_size, plus_results, label = "'+' operation", marker = "o", linestyle = "--")
plt.plot(input_size, join_results, label = "join method", marker = "o", linestyle = "--")
plt.legend()
plt.show()



