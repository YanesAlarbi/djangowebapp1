# from dask.widgets import get_template
# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models  import Member
from django.db.models import Q



# Create your views here.


def members(request):
    # return  HttpResponse("you are welcome in django world")
    mymembers=Member.objects.all().values()

    template=loader.get_template("all_members.html")
    context={
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember=Member.objects.get(id=id)
    template=loader.get_template("details.html")
    context={
        'mymember':mymember
    }

    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template("template.html")
    # amount=98.89
    greeting=1
    context={
        'amount':3.89,
        'average':95,
        'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
        'greeting':greeting,
        'mymembers':mymembers,
        'fruits':["Mango","Pineapple","Strawberries","Orange","Banana"],
        'fruits2': ["Mango", "Pineapple", "Strawberries", "Orange", "Banana"]
        ,"firstname":'Linus',
        'mylist':[99,99,97,97,97,95,96,96,92,97],
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Ford',
                'model': 'Sierra',
                'year': '1981',
            },
            {
                'brand': 'Volvo',
                'model': 'XC90',
                'year': '2016',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }]

        ,'emptyobject':[]

    }
    return HttpResponse(template.render(context, request))


def testview(request):
    mymembers=Member.objects.all().values()
    list_names=Member.objects.values_list('fname','join_date')
    filtered_data=Member.objects.filter(id=6).values()
    filtered_data2=Member.objects.filter(lname='ameen',id=7).values()
    # filtered_multiple=Member.objects.filter(fname='john').values()|Member.objects.filter(fname='jalal').values()
    filtered_multiple = Member.objects.filter(Q(fname='john' ) | Q(fname='jalal')).values()
    filedlookup_data=Member.objects.filter(fname__startswith='a').values()
    lookup_for_contains=Member.objects.filter(fname__contains='rri').values()
    lookup_for_icontains = Member.objects.filter(fname__icontains='RRI').values()
    lookupfields_endswith=Member.objects.filter(lname__endswith='n').values()
    lookupfields_iendswith=Member.objects.filter(lname__iendswith='N').values()
    #lf means lookupfields
    lf_exact=Member.objects.filter(lname__exact='Travolta').values()
    lf_iexact = Member.objects.filter(lname__iexact='Travolta').values()
    lf_in=Member.objects.filter(lname__in=['travolta','edward']).values()
    lf_isnull=Member.objects.filter(join_date__isnull=True).values()
    lf_gt = Member.objects.filter(id__gt=5).values()
    lf_gte=Member.objects.filter(id__gte=5).values()
    lf_quarter = Member.objects.filter(join_date__quarter=3).values()
    lf_range = Member.objects.filter(id__range=(4,6)).values()

    template=loader.get_template("testtemplate.html")
    context={
        'mymembers':mymembers,
        'list_names':list_names,
        'filtered_data':filtered_data,
        'filtered_data2':filtered_data2,
        'filtered_multiple':filtered_multiple,
        'filedlookup_data':filedlookup_data,
        'lookup_for_contains':lookup_for_contains,
        'lookup_for_icontains':lookup_for_icontains,
        'lookupfields_endswith':lookupfields_endswith,
        'lookupfields_iendswith':lookupfields_iendswith,
        'lf_exact':lf_exact,
        'lf_iexact':lf_iexact,
        'lf_in':lf_in,
        'lf_isnull':lf_isnull,
        'lf_gt':lf_gt,
        'lf_gte':lf_gte,
        'lf_quarter':lf_quarter,
        'lf_range':lf_range
    }
    return HttpResponse(template.render(context, request))

def test2(request):
    mymembers = Member.objects.all().values()
    orderbylist=Member.objects.all().order_by('-fname').values()
    moreorderbylist=Member.objects.all().order_by('fname','-id').values()

    template=loader.get_template("test2.html")
    context={

        'mymembers':mymembers,
        'orderbylist':orderbylist,
        'moreorderbylist':moreorderbylist,
        'fruits': ['Apple', 'Banana', 'Cherry'],



    }
    return  HttpResponse(template.render(context, request))




