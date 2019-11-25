"""Hamming Number Challenge."""


def ham():
    """Calculate First 8000 Hamming numbers."""
    ham_list = set()
    for i in range(20):
        for j in range(20):
            for k in range(20):
                ham_list.add(2**i * 3**j * 5**k)
    return sorted(ham_list, key=int)


def main():
    """Drive the example."""
    ham_list = ham()

    def is_ham(x):
        return x in ham_list

    print("First 25 hamming numbers\n", ham_list[:25])
    print("The 137th hamming number\n", ham_list[136])

    print("%d is ham? %s" % (1700, is_ham(1700)))
    print("%d is ham? %s" % (1215, is_ham(1215)))


if __name__ == "__main__":
    main()
