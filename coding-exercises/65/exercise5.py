for filename in [f'{x}.txt' for x in 'abc']:
    file = open(filename, 'r')
    print(file.read())