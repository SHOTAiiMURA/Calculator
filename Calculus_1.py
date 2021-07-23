from Calculator import BasicArithmeticOperation0_1 as BAO
# import BasicArithmeticOperation0_1 as BAO
import numpy as np
import time


def trapezium_area(top, base, height):
    area = BAO.multi(1 / 2, (BAO.multi(BAO.add(top, base), height)))
    return area


def integration_simp(equ, start, end, n):
    h = (end - start) / n

    x_values = np.arange(start, end + h, h)

    y_values = np.zeros(x_values.size)
    for i in range(y_values.size):
        y_values[i] = eval(equ.replace("X", str(x_values[i])))

    area = y_values[0] + y_values[-1] + 4 * (y_values[1:-1:2].sum()) + 2 * (y_values[2:-2:2].sum())
    return area * h / 3


def integration_trape(equ, start, end, n):
    h = (end - start) / n
    x_values = np.arange(start, end + h, h)
    area = 0

    y_values = np.zeros(x_values.size)
    for i in range(x_values.size):
        y_values[i] = eval(equ.replace("X", str(x_values[i])))

    for i in range(y_values.size - 1):
        area += trapezium_area(y_values[i], y_values[i + 1], h)

    return area

def decimal_to_fraction(num):
    #a/b
    for i in range(1, 10000):
        j = int(num * i)
        if num - j/i <= 0.00000000001:
            if i == 1:
                print(j)
                return str(j)
            else:
                print("{0}/{1}".format(j, i))
                return str(j) + "/"+str(i)
        elif (j+1)/i - num  <= 0.00000000001:
            if i == 1:
                print(j+1)
                return str(j)
            else:
                print("{0}/{1}".format(j+1, i))
                return str(j+1) + "/"+str(i)
    print(num)
    return str(num)

num = 0
num
decimal_to_fraction(2417.333333333333333)

start_time = time.time()
print("simpton : ")
print(decimal_to_fraction(integration_simp("X+2*X*X+4", 1, 15, 10)))

end_time = time.time()
print("Time Taken : ", end="")
print(end_time - start_time)

start_time = time.time()
print("trapesium : ")

print(decimal_to_fraction(integration_trape("X+2*X*X+4", 1, 15, 10000)))
end_time = time.time()
print("Time Taken : ", end="")
print(end_time - start_time)


