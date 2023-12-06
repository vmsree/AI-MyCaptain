n = int(input())
nums = list(int(x) for x in input().split())

positive_nums = []

for n in nums:
    if n >= 0:
        positive_nums.append(n)
        
print(positive_nums)
