"""
This is a utility script that load data for Codemera Test Project.

To run this script,
1) Set the appropiate file paths in the variables provincia_file and
    municipio_file (see below)
2) Open a python prompt in a console
    python manage.py shell
3) Run in the python prompt
    exec(open("./test_project/load_data_script.py").read())

Remember to reopen the python shell if you change the model.
"""

from csv import DictReader
from os import getcwd

from test_project.models import Province, Municipality, Zone

#Use these variables to set data files location
#provincia_file = 'E:/tmp/python_test_project_data/provincias.csv'
#municipio_file = 'E:/tmp/python_test_project_data/municipios.csv'
provincia_file = getcwd().replace('\\', '/') + \
    "/test_project/test_data/provincias.csv" 

municipio_file = getcwd().replace('\\', '/') + \
    "/test_project/test_data/municipios.csv" 

#Load Zone data
reader = DictReader(open(provincia_file))
for row in reader:
   #Extract zones from Province file. Only add a zone if it does not exists in
   #the database
   if len(Zone.objects.filter(code=row['ZONA'])) > 0:
        continue
   a_zone = Zone(code=row['ZONA'])
   a_zone.save()
   print('Zone added: ' + row['ZONA'])

#Load Province data
reader = DictReader(open(provincia_file))
for row in reader:
   #Extract provinces from Province file. Only add a province if
   #it does not exists in the database
   if len(Province.objects.filter(code=row['COD_HASC'])) > 0:
        continue
   a_zone = Zone.objects.get(code=row['ZONA'])
   a_zone.province_set.create(name=row['NOMBRE'], code=row['COD_HASC'])
   a_zone.save()

   print('Province added: ' + str(row['COD_HASC']) + ' ' + row['NOMBRE'])

#Load Municipality data
reader = DictReader(open(municipio_file))
for row in reader:
   #Extract provinces from municipality file. Only add a municipality if
   #it does not exists in the database
   if len(Municipality.objects.filter(code=row['COD_HASC'])) > 0:
        continue
   splitted_code = row['COD_HASC'].split('.')
   if (len(splitted_code) != 3):
        continue
   province_code = splitted_code[0] + '.' + splitted_code[1]
   the_province = Province.objects.get(pk=province_code)
   the_province.municipality_set.create(
        name=row['NOMBRE'], code=row['COD_HASC'])
   the_province.save()

   print('Municipality added: ' + row['NOMBRE'])