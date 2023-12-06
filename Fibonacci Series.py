fibonacii_series = [0, 1]

for x in range(0, 15):
    fibonacii_series.append(fibonacii_series[-1] + fibonacii_series[-2])
    
print(*fibonacii_series, sep=" ")
