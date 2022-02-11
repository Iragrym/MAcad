from prettytable import PrettyTable, from_csv

printer = PrettyTable()

with open('input.csv', 'r') as f:
    headers = f.readline().rstrip().split(',')
    printer.field_names = headers

    for line in f:
        items = line.rstrip().split(',')
        printer.add_row(items)

print(printer)
