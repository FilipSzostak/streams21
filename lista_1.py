
list = [1,2,4,3,67,54,12,23]

x = len(list)

while x > 1:
        zamien = False
        for i in range(0, x - 1):
            a = list[i]
            b = list[i+1]

            if b < a:
                a, b = b, a
                zamien = True

        x -= 1
        if zamien == False:
            break

print("Końcowa lista prezentuje się następująco:", list)
