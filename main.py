"""Hamming Number Challenge."""


def hamming(n):
    """Returns the nth hamming number."""

    ham_list = [1] * n

    x2, x3, x5 = 2, 3, 5
    i, j, k = 0, 0, 0
    for num in range(1, n):
        ham_list[num] = min(x2, x3, x5)
        if ham_list[num] == x2:
            i += 1
            x2 = 2 * ham_list[i]
        if ham_list[num] == x3:
            j += 1
            x3 = 3 * ham_list[j]
        if ham_list[num] == x5:
            k += 1
            x5 = 5 * ham_list[k]
    return ham_list[-1]


def main():
    """Drive the example."""

    print("First 25 hamming numbers :")
    for i in range(1, 25+1):
        print(hamming(i), end=', ')
    print()

    print("The 137th hamming number\n", hamming(137))

    lst = [hamming(h) for h in range(1, 1001)]

    print("%d is ham? %s" % (1700, 1700 in lst))
    print("%d is ham? %s" % (1215, 1215 in lst))


if __name__ == "__main__":
    main()
