arreglo = [1000000001, 1000000002, 10000]
def large_sum(ar):
    suma = 0
    for i in range(len(ar)):
        suma = suma + ar[i]

    return suma

print(f'The sum of array: {arreglo} is {large_sum(arreglo)}')
