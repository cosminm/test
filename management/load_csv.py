import sys, os, csv
from random import choice

def import_csv():
    csv_filename="OUTPUT.csv"
    djangoproject_home="/home/io/Projects/management/management/"

    sys.path.append(djangoproject_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

    from cms.models import Student, Profesor, Clasa

    clase = ('A', 'B', 'C', 'D', 'E', )
    for c in clase:
        record = Clasa()
        record.nume = c
        record.save()
        print 'Clasa ', record.nume, ' a fost salvata.'

    dataReader = csv.reader(open(csv_filename), delimiter=',')

    print "Importing...."

    for row in dataReader:
        if row[-1] == 'profesor':
            record = Profesor()

        if row[-1] == 'student':
            record = Student()

        record.nume = row[0]
        record.nume_utilizator = row[1]
        record.parola = row[2]
        record.adresa_domiciliu = row[3]
        record.adresa_corespondenta = row[4]
        record.telefon = row[5]

        if row[-1] == 'student':
            record.clasa = Clasa.objects.get(nume__exact=choice(clase))
        record.save()
        print "Record ", record.nume, "was added."

    print "The data was imported."



def main():
    import_csv()

if __name__ == '__main__':
    main()
