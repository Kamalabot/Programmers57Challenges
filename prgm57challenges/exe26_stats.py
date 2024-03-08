#Lets compute the statistics of a list 
import statistics
import math

print("""Enter a list of website loading times in seconds.
 If you are done, enter 'done'""")

web_time = []
while True:
    num_web = input("Enter the loading times? ")
    if num_web == 'done':
        break
    else:
        web_time.append(int(num_web))

print(f"The sum of the loading times is: {sum(web_time)}")
print(f"The average of the loading times is: {sum(web_time) / len(web_time)}")
print(f"The maximum of the loading times is: {max(web_time)}")
print(f"The minimum of the loading times is: {min(web_time)}")
print(f"The median of the loading times is: {sorted(web_time)[len(web_time) // 2]}")
print(f"The standard deviation of the loading times is: {round(statistics.stdev(web_time), 2)}")

mean = sum(web_time) / len(web_time)

mean_diff = [x - mean for x in web_time]

diff_squared = [x ** 2 for x in mean_diff]

diff_squared_mean = sum(diff_squared) / len(diff_squared)

print(f"The Mean squared error of the loading times is: {round(math.sqrt(diff_squared_mean), 2)}")