n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

count = 0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if (a[j] > a[j + 1]):
            s = a[j]
            a[j] = a[j + 1]
            a[j + 1] = s
            count += 1

print "Array has been sorted in", str(count), "swaps."
print "First element is: ", a[0]
print "Last element is: ", a[-1]
