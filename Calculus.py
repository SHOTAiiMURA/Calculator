from Calculator import BasicArithmeticOperation0_1 as BAO
# import BasicArithmeticOperation0_1 as BAO
import numpy as np
import time
import matplotlib.pyplot as plt

def trapezium_area(top, base, height):
    area = BAO.multi(1 / 2, (BAO.multi(BAO.add(top, base), height)))
    return area


def integration_simp(equ, start, end, n):
    h = (end-start)/(n)
    x_values = np.arange(start, end+h, h)

    area = 0
    print("size : " + str(x_values.size))
    for i in range(100):
        if i in [0, 49, 98, 99]:
            print("0", end="")
        elif i in [24, 48, 74]:
            print("5", end="")
        elif i == 23:
            print("2", end="")
        elif i == 73:
            print("7", end="")
        elif i == 97:
            print("1", end="")
        else:
            print("*", end="")

    print()
    y_values = np.zeros(x_values.size)
    # print(y_values.size)
    for i in range(x_values.size):
        y_values[i] = eval(equ.replace("X", str(x_values[i])))

    # print("-1 : " + str(y_values[-1]))
    # print("4 sum : " + str((y_values[2:-2].sum())))
    # print(y_values[2:-1])
    first = y_values[0]
    print("first : ", end = "")
    print(first)
    end = y_values[-1]
    print("end : ", end="")
    print(end)
    twice = 2*y_values[2:-2:2]
    print("twice : ", end="")
    print(twice)
    sum_twice = twice.sum()
    print("sum_twice : ", end="")
    print(sum_twice)
    four_times = 4*y_values[1:-1:2]
    print("four_times : ", end="")
    print(four_times)
    sum_four_times = four_times.sum()
    print("sum_four_times : ", end="")
    print(sum_four_times)

    area = y_values[0] + y_values[-1] + 2*y_values[2:-2:2].sum() + 4*y_values[1:-1:2].sum()
    return area / (3*n)


def integration_simp_check(equ, start, end, step):
    x_values = np.arange(start, end, step)
    area = 0
    # print(x_values)
    for i in range(100):
        if i in [0, 49, 98, 99]:
            print("0", end="")
        elif i in [24, 48, 74]:
            print("5", end="")
        elif i == 23:
            print("2", end="")
        elif i == 73:
            print("7", end="")
        elif i == 97:
            print("1", end="")
        else:
            print("*", end="")

    print()
    y_values = np.zeros(x_values.size)
    # print(y_values.size)
    for i in range(x_values.size):
        y_values[i] = eval(equ.replace("X", str(x_values[i])))
        # if i % (x_values.size // 100) == 0:
        #     print("*", end="")

    for i in range(y_values.size - 2):
        area += (y_values[i] + 4 * y_values[i + 1] + y_values[i + 2]) * step / 3

    return area

def integration_trape(equ, start, end, step):
    x_values = np.arange(start, end, step)
    area = 0
    # print(x_values)
    for i in range(100):
        if i in [0, 49, 98, 99]:
            print("0", end="")
        elif i in [24, 48, 74]:
            print("5", end="")
        elif i == 23:
            print("2", end="")
        elif i == 73:
            print("7", end="")
        elif i == 97:
            print("1", end="")
        else:
            print("*", end="")

    print()
    y_values = np.zeros(x_values.size)
    # print(y_values.size)
    for i in range(x_values.size):
        y_values[i] = eval(equ.replace("X", str(x_values[i])))

    for i in range(y_values.size - 1):
        area += trapezium_area(y_values[i], y_values[i + 1], step)
        # if i % (x_values.size // 100) == 0:
        #     print("*", end="")

    return area

# a = np.array([0, 1, 2, 3, 4])
# a_squared = a*a
# print(a_squared)
# a_2 = a_squared+2
# print(a_2)
# a_2_4 = a_2*4
# print(a_2_4)
#
# result = a_2[0] + a_2_4[1] + a_2[2] + a_2[1] + a_2_4[2] + a_2[3] + a_2[2] + a_2_4[3] + a_2[4]
# print(result/3)

# start_time = time.time()
# print("check\n" + str(integration_simp_check("X*X+2", 0, 5, 0.5)))
# end_time = time.time()
# print(end_time - start_time)
start_time = time.time()
print("simpton\n" + str(integration_simp("X*X", 1, 4, 10)))
end_time = time.time()
print(end_time - start_time)
start_time = time.time()
print(integration_trape("X*X", 0, 5, 0.001))
end_time = time.time()
print(end_time - start_time)
#
# x = np.zeros(10000)  # x軸の値
# y1 = np.zeros(x.size)  # y軸の値
#
# for i in range(x.size-2):
#     y1[i] = integration_simp("X*X+2", 0, 5, 5/(i+1))
# # figureを生成する
# fig = plt.figure()
#
# # axをfigureに設定する
# ax = fig.add_subplot(1, 1, 1)
#
# # axesにplot
# ax.plot(x, y1, "-", linewidth=1)
#
# # 表示する
# plt.show()