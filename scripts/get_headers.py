with open('../data/happiness-data.csv', 'r') as file:
    headers = file.readline().strip().split(',')
    i = 0
    for header in enumerate(headers,i):
        print(header)