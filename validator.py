import pyisbn


def valid(lsbn_13):
    result = pyisbn.validate(lsbn_13)
    return result
"""
if __name__ == '__main__':
    validIsbn = 0
    #295400
    start = 9786010000000
    for start in range(9786010000000,9786019999999):
        if valid(str(start)):
            validIsbn += 1
    print(validIsbn)
"""