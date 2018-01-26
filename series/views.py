from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from series.models import Serie
from series.serializers import SerieSerializer
from series import markovgen


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def pretty_print_POST(req):
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

@csrf_exempt
def texto_lista(request):
    if request.method == 'POST':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def prediccion_lista(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = SerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        markov = markovgen.Markov()

        for x in serializer.data:
            markov.addText(x["texto"])
        return JSONResponse(markov.cachee)

    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        markov = markovgen.Markov()

        for x in serializer.data:
            markov.addText(x["texto"])
        return JSONResponse(markov.cachee)



@csrf_exempt
def eliminar_texto(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            serie = Serie.objects.get(pk=data["id"])
        except Serie.DoesNotExist:
           return HttpResponse(status=404)
        serie.delete()
        return HttpResponse(status=204)

@csrf_exempt
def prediccion(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        markov = markovgen.Markov()
        for x in serializer.data:
            markov.addText(x["texto"])
        if(data["texto"] in markov.cachee):
            return JSONResponse(markov.cachee[data["texto"]])
        else:
            return HttpResponse(status=404)

@csrf_exempt
def serie_list(request):
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        markov = markovgen.Markov()
        for x in serializer.data:
            markov.addText(x["texto"])

        return JSONResponse(markov.cachee)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = SerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse({"rest":"ok"}, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def serie_listando(request):
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return JSONResponse(serializer.data)



@csrf_exempt
def serie_detail(request, pk):
#    try:
#        serie = Serie.objects.get(pk=pk)
#    except Serie.DoesNotExist:
#        return HttpResponse(status=404)

    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        markov = markovgen.Markov()
        for x in serializer.data:
            markov.addText(x["texto"])
        return JSONResponse(markov.cachee[pk])

#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = SerieSerializer(serie, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JSONResponse(serializer.data)
#        return JSONResponse(serializer.errors, status=400)

#    elif request.method == 'DELETE':
#        serie.delete()
#        return HttpResponse(status=204)

