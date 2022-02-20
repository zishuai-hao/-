# coding=utf-8

# 递归
def sum_array(array, index):
    if len(array) == index + 1:
        return array[index]
    else:
        return array[index] + sum_array(array, index + 1)






