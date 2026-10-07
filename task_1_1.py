def discriminant(a, b, c):
    global d
    d = b ** 2 - 4 * a * c
    return d


def solution(a, b, c):
    discriminant(a, b, c)

    if d < 0:
        return 'корней нет'
    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2
    else:
        x = - (b / (2 * a))
        return x


if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))
