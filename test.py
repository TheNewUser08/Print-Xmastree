def print_tree(n):
    time = 0
    leaves = '#'
    lenw = -1
    while True:
        time += 1
        lenw += 2
        if time > n: break
        leaves = '#'*lenw
        if 2*n % 2 == 0:
            print(leaves.center(2*len(range(n))+1, '_'))
        else:
            print(leaves.center(2*len(range(n)), '_'))
    leaves = '#'
    if 2*n % 2 == 0:
        print(leaves.center(2*len(range(n))+1, '_'))
        print(leaves.center(2*len(range(n))+1, '_'))
    else:
        print(leaves.center(2*len(range(n)), '_'))
        print(leaves.center(2*len(range(n)), '_'))

print_tree(5)