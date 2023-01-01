def hanio(n, a, b, c):
    """
    :param n:  初始时A柱上的盘子数
    :param a:  起始盘子所在的柱子
    :param b:  中转柱子
    :param c:  目的地柱子
    :return:
    """
    if n > 0:
        hanio(n-1, a, c, b)
        print("盘子从%s移动到%s" % (a, c))
        hanio(n-1, b, a, c)


if __name__ == '__main__':
    hanio(3, 'A', 'B', 'C')