def numbers(num):
    """
    Counts the right figures for the triangle
    :param num: number of the rows in Pascal triangle
    :return: r
    """
    r = []
    for i in range(num):
        d = len(r)
        r = [1 if i == 0 or i == d else r[i-1]+r[i] for i in range(d+1)]
        yield r


def triangle(num):
    """
    Makes triangle looks like a triangle
    :param num: number of the rows in Pascal triangle
    :return: None
    """
    a = list(numbers(num))
    m = len('    '.join(map(str, a[-1])))
    for x in a:
        print('    '.join(map(str, x)).center(m)+'\n')


num = int(input())
list(numbers(num))
triangle(num)
