from django.core.management.base import BaseCommand
from optparse import make_option
from reporteaccidentes.accidentes.helpers.shapefile import Reader
from reporteaccidentes.accidentes.helpers.utmToLatLng import utmToLatLng
from reporteaccidentes.accidentes.models import Accidente


class Command(BaseCommand):
    args = ''
    help = 'Imports data from a Shapefile container.'
    option_list = BaseCommand.option_list + (
        make_option('--shapefile_file',
            help='Shapefile directory path'),
        )

    def handle(self, *args, **options):
        shapefile_directory = options['shapefile_file']
        print 'Importing data'
        sf = Reader(shapefile_directory)
        iterator_number = 0
        for rec in sf.records():
            accident = Accidente()
            accident.calle = rec[0]
            accident.cruce = rec[1]
            accident.tipo = rec[2]
            accident.year = rec[3]
            accident.nombre_calle = rec[4]
            accident.nombre_cruce = rec[5]
            accident.esquina = rec[6]
            accident.latititud, accident.longitude = utmToLatLng(21,
                                            sf.shape(iterator_number).points[0][0],
                                            sf.shape(iterator_number).points[0][1],
                                            False)
            accident.save()
            iterator_number += 1
        print 'Done'
