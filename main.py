import random
import numpy as np

'''计算均值'''
def mean(x):
    return sum(x) / len(x)

'''计算偏差'''
def derta(x):
    x_bar = mean(x)
    result = [x_i - x_bar for x_i in x]
    return result

'''计算协方差'''
def covariance(a, b):
    dot_list = [a_i * b_i for a_i, b_i in zip(derta(a), derta(b))]
    dot_result = mean(dot_list)
    return dot_result

'''计算标准差'''
def std(x):
    return np.sqrt(mean(([derta_x ** 2 for derta_x in derta(x)])))

'''计算相关系数'''
def pearson(x, y):
    result = covariance(x, y) / (std(x) * std(y))
    return result

'''计算相关系数矩阵'''
def correaltion_matrix(x):
    num_x = len(x)
    matrix = np.zeros([num_x, num_x])

    for i in range(num_x):
        for j in range(num_x):
            matrix[i][j] = pearson(x[i], x[j])

    return matrix

'''随机生成变量进行测试'''
X = [random.randint(-20, 100) for _ in range(25)]
Y = [random.randint(-20, 100) for _ in range(25)]
Z = [random.randint(-20, 100) for _ in range(25)]

print("复现的函数计算皮尔逊相关系数矩阵：\n", correaltion_matrix([X, Y, Z]))
print("调用内置函数计算皮尔逊相关系数矩阵：\n", np.corrcoef([X, Y, Z]))
