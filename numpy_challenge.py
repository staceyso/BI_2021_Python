import numpy as np
if __name__ == "__main__":
    x = np.random.random(10)
    print(x)
    y = np.arange(10)
    print(y)
    z = np.zeros(10)
    print(z)


def matrix_multiplication(m1, m2):
    if m1.shape[1] != m2.shape[0]:
        print('It is impossible to multiply these matrices! For matrix multiplication, '
              'the number of columns in the first matrix must be equal to the number of rows in the second matrix.')
        return None
    else:
        m3 = m1 * m2
        return m3


def multiplication_check(lst):
    c = 0
    for i in range(len(lst)-1):
        if lst[i].shape[1] != lst[i+1].shape[0]:
            c += 1
    if c == 0:
        return True
    else:
        return False


def multiply_matrices(lst):
    if multiplication_check(lst):
        m = lst[0]
        for i in range(1, len(lst)):
            m *= lst[i]
        return m
    else:
        return None


def compute_2d_distance(a1, a2):
    return np.sqrt((a2[0] - a1[0]) ** 2 + (a2[1] - a1[1]) ** 2)


def compute_multidimensional_distance(a1, a2):
    a1 = np.array(a1)
    a2 = np.array(a2)
    return np.sqrt(sum((a2 - a1)**2))


def compute_pair_distances(m):
    m = np.array(m)
    n = m.shape[0]
    z = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            z[i][j] = compute_multidimensional_distance(m[i], m[j])
    return z
