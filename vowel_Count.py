str = input("Enter a sentence:")
lstr = str.lower()
vowel = "aeiou"
count = 0
for i in lstr:
    if count == 2:
        if i in vowel:
            count+1
            flag = False
            if count > 1:
                for i in range:
                    if (count % i) == 0:
                        flag = True
                        break
            if flag:
                print(count, "is not a prime number")
            else:
                print(count, "is a prime number")

print(count)