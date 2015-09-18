from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):

    if 'dobleS' in request.POST:
        print('')
    if 'trampaD' in request.POST:
        print('')
    if 'unidadS' in request.POST:
        print('')
    if 'reactancia' in request.POST:
        print('')
    template = loader.get_template('calculus/indexCalc.html')
    return HttpResponse(template.render())

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
