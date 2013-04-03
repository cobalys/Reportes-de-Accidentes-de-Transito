# -*- coding: utf-8 -*-
from django.db import connection
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template


def index(request):
    t = get_template('index.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)


def get_top(request):
    YEAR = {
           '2006': '2006',
           '2007': '2007',
           '2008': '2008',
           '2009': '2009',
           '2010': '2010',
    }
    TIPO = {
           '1': 'FATAL',
           '2': 'GRAVE',
           '3': 'LEVE',
    }
    cursor = connection.cursor()
    try:
        cantidad = int(request.GET.get('cantidad'))
    except:
        cantidad = 10
    tipo = str(request.GET.get('tipofilter', None))
    year = str(request.GET.get('yearfilter', None))
    year = YEAR.get(year, None)
    tipo = TIPO.get(tipo, None)
    if tipo is not None:
        if year is not None:
            query = '''
            SELECT nombre_calle, nombre_cruce, count(*) AS cantidad, latititud, longitude, year
            FROM accidentes_accidente 
            WHERE year LIKE %s AND tipo LIKE %s 
            GROUP BY nombre_calle, nombre_cruce, latititud, longitude, year
            HAVING count(*) >= %s 
            ORDER BY year DESC, count(*) DESC;
            '''
            cursor.execute(query, [year, tipo, cantidad])
            rows = cursor.fetchall()
        else:
            query = '''
            SELECT nombre_calle, nombre_cruce, count(*) AS cantidad, latititud, longitude 
            FROM accidentes_accidente 
            WHERE tipo LIKE %s 
            GROUP BY nombre_calle, nombre_cruce, latititud, longitude 
            HAVING count(*) >= %s
            ORDER BY count(*) DESC;
            '''
            cursor.execute(query, [tipo, cantidad])
            rows = cursor.fetchall()
    else:
        if year is not None:
            query = '''
            SELECT nombre_calle, nombre_cruce, count(*) AS cantidad, latititud, longitude, year
            FROM accidentes_accidente 
            WHERE year LIKE %s 
            GROUP BY nombre_calle, nombre_cruce, latititud, longitude, year
            HAVING count(*) >= %s
            ORDER BY year DESC, count(*) DESC;
            '''
            cursor.execute(query, [year, cantidad])
            rows = cursor.fetchall()
        else:
            query = '''
            SELECT nombre_calle, nombre_cruce, count(*) AS cantidad, latititud, longitude 
            FROM accidentes_accidente 
            GROUP BY nombre_calle, nombre_cruce, latititud, longitude 
            HAVING count(*) >= %s
            ORDER BY count(*) DESC;
            '''
            cursor.execute(query, [cantidad,])
            rows = cursor.fetchall()
    cursor.close()
    output = list()
    output.append("[")
    for row in rows:
        print row
        output.append("['Aqui hubo %s Accidentes.', %s, %s],"% (unicode(row[2]),unicode(row[3]),unicode(row[4]),))
    output.append("];")
    return HttpResponse("".join(output))


def about(request):
    variables = dict()
    t = get_template('acerca-de.html')
    html = t.render(RequestContext(request, variables))
    return HttpResponse(html)


def top(request):
    cursor = connection.cursor()
    query = '''
            SELECT nombre_calle, nombre_cruce, COUNT(*) as cantidad 
            FROM accidentes_accidente group by nombre_calle,nombre_cruce 
            ORDER BY COUNT(*) DESC LIMIT 20;
            '''
    cursor.execute(query)
    rows = cursor.fetchall()
    variables = dict()
    variables['rows'] = rows
    cursor.close()
    t = get_template('ranking.html')
    html = t.render(RequestContext(request, variables))
    return HttpResponse(html)
