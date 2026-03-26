s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

words1 = s1.split()
words2 = s2.split()

uncommon = []

for word in words1:
    if word not in words2:
        uncommon.append(word)

for word in words2:
    if word not in words1:
        uncommon.append(word)

print("Uncommon words:", uncommon)
