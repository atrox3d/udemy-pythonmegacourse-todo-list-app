for filename in [f'file{n}.txt' for n in range(5)]:
    print(filename)
    file = open(filename, 'w')
    file.write('Hello')
    file.close()
