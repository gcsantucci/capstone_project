files = 'pdkdata_1.csv'
new = 'pdkdata_1.csv.new'

new_line = []
with open(files, 'r') as inf:
    with open(new, 'w') as f:
        for line in inf:
            line = line.strip().split(',')
            new_line = line[:-2]
            new_line.append(line[-1])
            line = new_line[:-2]
            line.append(new_line[-1])
            f.write(','.join(line)+'\n')
