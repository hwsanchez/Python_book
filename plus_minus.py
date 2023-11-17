def plusMinus(arr):
    # Write your code here
    pos_prop = 0
    neg_prop = 0
    zero_prop = 0
    size = len(arr)
    for i in range(size):
        if arr[i] > 0:
            print(f'positivo: {arr[i]}')
            pos_prop += 1
            print(f'number of positive: {pos_prop}')
        elif arr[i] < 0:
            neg_prop += 1
        else:
            zero_prop += 1
    print(round(pos_prop/size, 6))
    print(round(neg_prop/size, 6))
    print(round(zero_prop/size, 6))
arreglo = [1,1,0,-1,-1]
plusMinus(arreglo)
