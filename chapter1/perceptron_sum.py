import numpy as np

nand_w = np.asarray([-2,-2])
nand_b = 3

def nand_perceptron_predict(x):
    return 0 if np.dot(nand_w,x) + nand_b <= 0 else 1

def perceptron_sum(x):
    x1, x2 = x
    res_1_1 = nand_perceptron_predict(x)
    res_2_1 = nand_perceptron_predict([x1, res_1_1])
    res_2_2 = nand_perceptron_predict([x2, res_1_1])
    bitwise_sum = nand_perceptron_predict([res_2_1, res_2_2])
    carry_bit = nand_perceptron_predict([res_1_1, res_1_1])

    return carry_bit, bitwise_sum

for x1 in range(2):
    for x2 in range(2):
        print("{} + {} = {}".format(x1,x2,perceptron_sum([x1, x2])))
