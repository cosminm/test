import csv
import sys

fields = ('nume', 'utilizator', 'parola', 'adr_dom', 'adr_cores', 'tel', )
rol = ('student', 'profesor', )
n_fields = len(fields)
num_rows = 20000
filename = 'OUTPUT.csv'


def generate_row(row_index, rol_index):
    row = []
    for i in range(n_fields):
        row.append(fields[i]+'_'+str(row_index))
    row.append(rol[rol_index])
    return row


def write_rows():
    f = open(filename, 'wb')
    csv_w = csv.writer(f)
    num_prof = num_rows / 100
    num_stud = num_rows - num_prof
    [csv_w.writerow(generate_row(i,1)) for i in xrange(num_prof)]
    [csv_w.writerow(generate_row(i,0)) for i in xrange(num_stud)]
    f.close()


def main():
    write_rows()

if __name__ == '__main__':
    main()
