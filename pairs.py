

n, k = map(int, input().split())
arr = list(map(int, input.split()))
memo = set()
count = 0

for a in arr:
    if a + k in memo:
        count += 1
    if a - k in memo:
        count += 1

    memo.add(a)
print(count)
