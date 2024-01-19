i = 3
ii = 5
multiples = []

while i < 1000:
    multiples.append(i)
    i += 3

while ii < 1000:
    multiples.append(ii)
    ii += 5

print("Sum of all the multiples of 3 or 5 below 1000 is", sum(multiples))

