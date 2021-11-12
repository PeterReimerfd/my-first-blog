from functools import singledispatch
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import DFrame
from django.db.models import Avg, Sum, Max, Min, Case, When, StdDev, F, Count, Case, Q, query
from django.utils import timezone
from django.contrib import messages
from .utils import get_field_columns
from django.db import connection, reset_queries
#from .forms import PostForm
import json
import csv, io

# Create your views here.

def data(request):
    # Set up the initial query
    query = DFrame.objects.all()

    # set up some initial filterable values
    context = {
        "filter_fields": DFrame.filterable_fields,
        "filter_columns": None,
        "current_filters": {}
    }

    # get the currnet filter values
    filter_field = request.GET.get("field")
    filter_value = request.GET.get("value")
    filter_op = request.GET.get("op")

    # pass the existing values into the context so they're available in the template
    context["current_filters"]["field"] = filter_field
    context["current_filters"]["value"] = filter_value
    if filter_field is not None:
        # we already have a filter field, populate the columns drop down
        context["filter_columns"] = get_field_columns(filter_field)

        if filter_field not in DFrame.filterable_fields:
            return HttpResponseBadRequest()

        if filter_value is not None:
            filter_by = filter_field
            # Ensure that the field being filtered on is actually allowed

            # python magic kwargs to build the filter
            # this is the equivalent of doing query.filter(name="Name One") (for example)
            if filter_op is not None:
                filter_by = filter_by + "__" + filter_op
                context["current_filters"]["op"] = filter_op
            query = query.filter(**{filter_by: filter_value}) 

    context["data"] = query
    print(context)

    return render(request, 'blog/data.html', context)

def get_columns(request):
    field = request.GET.get("field")

    # Make sure the required argument was passed in and is an available field to filter on
    if field is None or field not in DFrame.filterable_fields:
        return HttpResponseBadRequest(json.dumps({"message": "Bad field provided"}), content_type="application/json")

    # send the frontend the filter columns, as JSON
    filter_columns = get_field_columns(field)
    return HttpResponse(json.dumps(filter_columns), content_type="application/json")

def delete_all(request):
    DFrame.objects.all().delete()
    tuble = DFrame.objects.all()
    return render(request, 'blog/check_csv.html',{'tuble': tuble})

def dataframe(request):
    print('some shit')
    x=DFrame.objects.all()
    return(HttpResponse(print(x)))

#def post_list(request):
#    posts = Post.objects.all().order_by('published_date')
#    print(posts.first().text)
#    return render(request,'blog/post_list.html',{'posts': posts})

def check_csv(request):
    tuble = DFrame.objects.all()
    y=DFrame.objects.all().aggregate(Avg('rangelow'))
    x=DFrame.objects.all().values('location').annotate(ARL=Avg('rangelow'))
    print(y)
    print(x)
    #tuble=DFrame.objects.all().filter(location='KC')
    return render(request, 'blog/check_csv.html',{'tuble': tuble})

def test_filter(request):
    DFrame.objects.filter(prosecuter="McCracken. Sheri").update(prosecuter="Catania. Sheri")
    #gonna need some gets here
    #at any rate
    noto=request.GET.get("noto")
    f=request.GET.get("firstparam")
    s=request.GET.get("seg")
    o=request.GET.get("outtie")
    sp=request.GET.get("secondparam")
    fstat=request.GET.get("fstat")
    ptype=request.GET.get("ptype")
    u924c=request.GET.get("u924c")
    ptr=request.GET.get("ptr")
    aw=request.GET.get("aw")
    res=request.GET.get("res")
    plap=request.GET.get("plap")
    mofi=request.GET.get("mofi")
    mowo=request.GET.get("mowo")
    psrof=request.GET.get("psrof")
    psrow=request.GET.get("psrow")
    smf=request.GET.get("smf")
    coop=request.GET.get("coop")
    cbas=request.GET.get("cbas")
    vaap=request.GET.get("vaap")
    ccst=request.GET.get("ccst")
    ccfe=request.GET.get("ccfe")
    manmin=request.GET.get("manmin")
    efo=request.GET.get("efo")
    ntfc=request.GET.get("ntfc")
    fboo=request.GET.get("fboo")
    exem=request.GET.get("exem")
    iiw=request.GET.get("iiw")
    cfrec=request.GET.get("cfrec")
    psrw=request.GET.get("psrw")
    pros=request.GET.get("pros")
    atto=request.GET.get("atto")
    gle1=request.GET.get("gle1")
    gle2=request.GET.get("gle2")
    gle3=request.GET.get("gle3")
    gle4=request.GET.get("gle4")
    gle5=request.GET.get("gle5")
    gle6=request.GET.get("gle6")
    gle7=request.GET.get("gle7")
    lowgui=request.GET.get("lowgui")
    highgui=request.GET.get("highgui")
    marmot=request.GET.get("marmot")
    senim=request.GET.get("senim")
    suprel=request.GET.get("suprel")
    prob=request.GET.get("prob")
    coreper=request.GET.get("coreper")
    gregor=request.GET.get("gregor")
    startdt=request.GET.get("startdt")
    enddt=request.GET.get("enddy")
    chcat=request.GET.get("chcat")
    coureject=request.GET.get("coureject")
    aolevel=request.GET.get("aolevel")
    gle35=request.GET.get("gle35")
    altcoin=0
    title=o
    sargh="x"
    if o == "sentenceimprovement":
        o = "rangelow"
        altcoin = "sentenceimposed"
        title = "Sentence Improvement"
        sargh = "sentenceimprovement"
    if o == "sip":
        o = "rangelow"
        altcoin = "sentenceimposed"
        title = "Sentence Improvement"
        sargh = "sip"
    if s == "prosecuter":
        stitling = "prosecutor"
    else:
        stitling = s
    ntitle = "Counter-"
    otitle = "Total "
    if title is not None:
        if sargh == "sip":
            title = "Sentence Improvement (percentage)"
            ntitle = "Counter-" + title
            otitle = "Total " + title
        else:
            title = title + " (in months)"
            ntitle = "Counter-" + title
            otitle = "Total " + title
    
    #Below, filter management FOR DROPDOWN FILTERS
    tuble = DFrame.objects.all()
    segtub = DFrame.objects.all()
    nuble = DFrame.objects.all()
    if f != "SPACE":
        tuble = tuble.filter(location=f)
    if sp != "SPACE":
        tuble = tuble.filter(judge=sp)
    if fstat != "SPACE":
        tuble = tuble.filter(statue=fstat)
    if ptype != "SPACE":
        tuble = tuble.filter(pleatype=ptype)
    if u924c != "SPACE":
        if u924c == "NO":
            tuble = tuble.filter(unfiled924c=u924c) | tuble.filter(unfiled924c="UNKNOWN")
        else:
            tuble = tuble.filter(unfiled924c=u924c)
    if ptr != "SPACE":
        if ptr != "detain":
            if ptr != "release":
                tuble = tuble.filter(pretrialrelease=ptr)
    if ptr == "release":
        tuble = tuble.filter(pretrialrelease__startswith="Released")
    if ptr == "detain":
        tuble = tuble.filter(pretrialrelease__startswith="Detained")
    if aw != "SPACE":
        if aw == "YES":
            tuble = tuble.filter(appealwaiver=aw)
        else:
            tuble = tuble.filter(appealwaiver=aw) | tuble.filter(appealwaiver="N/A")
    if res != "SPACE":
        if res == "YES":
            tuble = tuble.filter(restitution=res)
        else:
            tuble = tuble.filter(restitution=res) | tuble.filter(restitution="") | tuble.filter(restitution="UNKNOWN")
    if plap != "SPACE":
        tuble = tuble.filter(plantoappeal=plap)
    if mofi != "SPACE":
        if mofi == "No":
            tuble = tuble.filter(motionsfiled=mofi) | tuble.filter(motionsfiled="UNKNOWN")
        else:
            tuble = tuble.filter(motionsfiled=mofi)
    if mowo != "SPACE":
        if mowo == "No":
            tuble = tuble.filter(motionswon=mowo) | tuble.filter(motionswon="UNKNOWN")
        else:
            tuble = tuble.filter(motionswon=mowo)
    if psrof != "SPACE":
        if psrof == "NO":
            tuble = tuble.filter(psrobjectionsfiled=psrof) | tuble.filter(psrobjectionsfiled="UNKNOWN")
        else:
            tuble = tuble.filter(psrobjectionsfiled=psrof)
    if psrow != "SPACE":
        if psrow == "NO":
            tuble = tuble.filter(psrobjectionswon=psrow) | tuble.filter(psrobjectionswon="UNKNOWN")
        else:
            tuble = tuble.filter(psrobjectionswon=psrow)
    if smf != "SPACE":
        if smf == "NO":
            tuble = tuble.filter(sentencingmemofiled=smf) | tuble.filter(sentencingmemofiled="UNKNOWN")
        else:
            tuble = tuble.filter(sentencingmemofiled=smf)
    if coop != "SPACE":
        if coop == "NO":
            tuble = tuble.filter(cooperation=coop) | tuble.filter(cooperation="UNKNOWN")
        else:
            tuble = tuble.filter(cooperation=coop)
    if cbas != "SPACE":
        if cbas == "NO":
            tuble = tuble.filter(chargebargainaffectingsentencing=cbas) | tuble.filter(chargebargainaffectingsentencing="UNKNOWN") | tuble.filter(chargebargainaffectingsentencing="N/A")
        else:
            tuble = tuble.filter(chargebargainaffectingsentencing=cbas)
    if vaap != "SPACE":
        if vaap == "NO":
            tuble = tuble.filter(variance=vaap) | tuble.filter(variance="UNKNOWN") | tuble.filter(variance="N/A")
        else:
            tuble = tuble.filter(variance=vaap)
    if ccst != "SPACE":
        if ccst == "NO":
            tuble = tuble.filter(cctostate=ccst) | tuble.filter(cctostate="UNKNOWN") | tuble.filter(cctostate="N/A")
        else:
            tuble = tuble.filter(cctostate=ccst)
    if ccfe != "SPACE":
        if ccfe == "NO":
            tuble = tuble.filter(cctofederal=ccfe) | tuble.filter(cctofederal="UNKNOWN") | tuble.filter(cctofederal="N/A")
        else:
            tuble = tuble.filter(cctofederal=ccfe)
    if manmin != "SPACE":
        if manmin == "NO":
            tuble = tuble.filter(mandatoryminimumimposed=manmin) | tuble.filter(mandatoryminimumimposed="UNKNOWN")
        else:
            tuble = tuble.filter(mandatoryminimumimposed=manmin)
    if efo != "SPACE":
        tuble = tuble.filter(eightfiveone=efo)
    if ntfc != "SPACE":
        tuble = tuble.filter(ninetwofoure=ntfc)
    if fboo != "SPACE":
        tuble = tuble.filter(fourbonepointone=fboo)
    if exem != "SPACE":
        if exem == "NO":
            tuble = tuble.filter(expertemployed=exem) | tuble.filter(expertemployed="UNKNOWN")
        else:
            tuble = tuble.filter(expertemployed=exem)
    if iiw != "SPACE":
        if iiw == "NO":
            tuble = tuble.filter(investigatorinterviewedwitness=iiw) | tuble.filter(investigatorinterviewedwitness="UNKNOWN")
        else:
            tuble = tuble.filter(investigatorinterviewedwitness=iiw)
    if cfrec != "SPACE":
        tuble = tuble.filter(courtfollowedrecommendationofnonbindingpleaagreement=cfrec)
    if chcat != "SPACE":
        tuble = tuble.filter(criminalhistorycategory=chcat)
    if coureject != "SPACE":
        tuble = tuble.filter(courtrejectedinitialbindingplea=coureject)
    #Below, filter management for TYPED filters
    if psrw is not None:
        tuble = tuble.filter(psrwriter__startswith=psrw)
    if pros is not None:
        tuble = tuble.filter(prosecuter__startswith=pros)
    if atto is not None:
        tuble = tuble.filter(attorney__startswith=atto)
    #Below, filter management for ORDINAL filters
    if lowgui is not None:
        if gle1 == "less":
            tuble = tuble.filter(rangelow__lte=lowgui)
        if gle1 == "more":
            tuble = tuble.filter(rangelow__gte=lowgui)
        if gle1 == "exact":
            tuble = tuble.filter(rangelow = lowgui)
    if highgui is not None:
        if gle2 == "less":
            tuble = tuble.filter(rangelow__lte=highgui)
        if gle2 == "more":
            tuble = tuble.filter(rangelow__gte=highgui)
        if gle2 == "exact":
            tuble = tuble.filter(rangelow = highgui)
    if marmot is not None:
        if gle3 == "less":
            tuble = tuble.filter(rangelow__lte=marmot)
        if gle3 == "more":
            tuble = tuble.filter(rangelow__gte=marmot)
        if gle3 == "exact":
            tuble = tuble.filter(rangelow = marmot)
    if aolevel is not None:
        if gle35 == "less":
            tuble = tuble.filter(rangelow__lte=aolevel)
        if gle35 == "more":
            tuble = tuble.filter(rangelow__gte=aolevel)
        if gle35 == "exact":
            tuble = tuble.filter(rangelow = aolevel)
    if senim is not None:
        if gle4 == "less":
            tuble = tuble.filter(rangelow__lte=senim)
        if gle4 == "more":
            tuble = tuble.filter(rangelow__gte=senim)
        if gle4 == "exact":
            tuble = tuble.filter(rangelow = senim)
    if suprel is not None:
        if gle5 == "less":
            tuble = tuble.filter(rangelow__lte=suprel)
        if gle5 == "more":
            tuble = tuble.filter(rangelow__gte=suprel)
        if gle5 == "exact":
            tuble = tuble.filter(rangelow = suprel)
    if prob is not None:
        if gle6 == "less":
            tuble = tuble.filter(rangelow__lte=prob)
        if gle6 == "more":
            tuble = tuble.filter(rangelow__gte=prob)
        if gle6 == "exact":
            tuble = tuble.filter(rangelow = prob)
    if coreper is not None:
        if gle7 == "less":
            tuble = tuble.filter(rangelow__lte=coreper)
        if gle7 == "more":
            tuble = tuble.filter(rangelow__gte=coreper)
        if gle7 == "exact":
            tuble = tuble.filter(rangelow = coreper)
    if startdt is not None:
        if startdt != "":
            tuble=tuble.filter(closingdate__gte=startdt)
    if enddt is not None:
        if enddt != "":
            tuble=tuble.filter(closingdate__lte=enddt)

    #Negated table creation
    nuble=nuble.exclude(num__in=tuble.values_list('num',flat=True))
    if noto == "on":
        holdem=tuble
        tuble=nuble
        nuble=holdem
    segnub=nuble
    overall=DFrame.objects.all()

    #Below, segmenting management
    segtct = DFrame.objects.all()
    segnct = DFrame.objects.all()
    overct = DFrame.objects.all()
    si=F('rangelow') - F('sentenceimposed') + 0.0
    simpall = DFrame.objects.all()
    simpleave = DFrame.objects.all()
    tublet = tuble.filter(rangelow__gt=0)
    overallet = overall.filter(rangelow__gt=0)
    nublet = nuble.filter(rangelow__gt=0)
    if gregor == "average":
        if sargh == "sip":
            simpleave = tublet.aggregate(tAgg=Avg(si/F('rangelow')+0.0))
            simpall = overallet.aggregate(tAgg=Avg(si/F('rangelow')+0.0))
        elif sargh == 'sentenceimprovement':
            simpleave = tublet.aggregate(tAgg=(Avg(o)-Avg(altcoin)))
            simpall = overallet.aggregate(tAgg=(Avg(o)-Avg(altcoin)))
        else:
            simpleave = tuble.aggregate(tAgg=(Avg(o)-Avg(altcoin)))
            simpall = overall.aggregate(tAgg=(Avg(o)-Avg(altcoin)))
    if gregor == "total":
        if sargh == "sip":
            simpleave = tublet.aggregate(tAgg=(Sum(si/(F('rangelow')+0.0))))
            simpall = overallet.aggregate(tAgg=(Sum(si)/Avg(F('rangelow')+0.0)))
        elif sargh == "sentenceimprovement":
            simpleave = tublet.aggregate(tAgg=(Sum(o)-Sum(altcoin)))
            simpall = overallet.aggregate(tAgg=(Sum(o)-Sum(altcoin)))
        else:
            simpleave = tuble.aggregate(tAgg=(Sum(o)-Sum(altcoin)))
            simpall = overall.aggregate(tAgg=(Sum(o)-Sum(altcoin)))
    if gregor == "maximum":
        if sargh == "sentenceimprovement":
            simpleave = tublet.aggregate(tAgg=(Max((si))))
            simpall = overallet.aggregate(tAgg=(Max((si))))
        elif sargh == "sip":
            simpleave = tublet.aggregate(tAgg=(Max((si/F('rangelow')+0.0))))
            simpall = overallet.aggregate(tAgg=(Max((si/F('rangelow')+0.0))))
        else:
            simpleave = tuble.aggregate(tAgg=(Max((o))))
            simpall = overall.aggregate(tAgg=(Max((o))))
    if gregor == "minimum":
        if sargh == "sentenceimprovement":
            simpleave = tublet.aggregate(tAgg=(Min(si)))
            simpall = overallet.aggregate(tAgg=(Min(si)))
        elif sargh == "sip":
            simpleave = tublet.aggregate(tAgg=(Min((si/F('rangelow')+0.0))))
            simpall = overallet.aggregate(tAgg=(Min((si/F('rangelow')+0.0))))
        else:
            simpleave = tuble.aggregate(tAgg=(Min(o)))
            simpall = overall.aggregate(tAgg=(Min(o)))
    if gregor == "standev":
        if sargh == "sentenceimprovement":
            simpleave = tublet.aggregate(tAgg=(StdDev(si)))
            simpall = overallet.aggregate(tAgg=(StdDev(si)))
        elif sargh == "sip":
            simpleave = tublet.aggregate(tAgg=(StdDev(si/F('rangelow')+0.0)))
            simpall = overallet.aggregate(tAgg=(StdDev(si/F('rangelow')+0.0)))
        else:
            simpleave = tuble.aggregate(tAgg=(StdDev(o)))
            simpall = overall.aggregate(tAgg=(StdDev(o)))
    simpleavect = tuble.count()
    simpallct = overall.count()
    if sargh == "sip":
        simpleavect = tublet.count()
        simpallct = overallet.count()
    if sargh == "sentenceimprovement":
        simpleavect = tublet.count()
        simpallct = overallet.count()
        #BELOW SIP STILL NEEDS IMPLEMENTATION, also TUBLET and OVERALLET for SENTENCEIMPROVEMENT
    if s != "SPACE":
        if s != None:
            if gregor == "average":
                if sargh == "sip":
                    segtub = tublet.values(s).annotate(tAgg=Avg(si/F('rangelow')+0.0)).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=Avg(si/F('rangelow')+0.0)).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=Avg(si/F('rangelow')+0.0)).annotate(tarct=Count(o))
                elif sargh == "sentenceimprovement":
                    segtub = tublet.values(s).annotate(tAgg=(Avg(o)-Avg(altcoin))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(Avg(o)-Avg(altcoin))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(Avg(o)-Avg(altcoin))).annotate(tarct=Count(o))
                else:
                    segtub = tuble.values(s).annotate(tAgg=(Avg(o)-Avg(altcoin))).annotate(tarct=Count(o))
                    segnub = nuble.values(s).annotate(nAgg=(Avg(o)-Avg(altcoin))).annotate(tarct=Count(o))
                    overall = overall.values(s).annotate(oAgg=(Avg(o)-Avg(altcoin))).annotate(tarct=Count(o))
            if gregor == "total":
                if sargh == "sentenceimprovement":
                    segtub = tublet.values(s).annotate(tAgg=(Sum(o)-Sum(altcoin))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(Sum(o)-Sum(altcoin))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(Sum(o)-Sum(altcoin))).annotate(tarct=Count(o))
                elif sargh == "sip":
                    segtub = tublet.values(s).annotate(tAgg=(Sum(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(Sum(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(Sum(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                else:
                    segtub = tuble.values(s).annotate(tAgg=(Sum(o)-Sum(altcoin))).annotate(tarct=Count(o))
                    segnub = nuble.values(s).annotate(nAgg=(Sum(o)-Sum(altcoin))).annotate(tarct=Count(o))
                    overall = overall.values(s).annotate(oAgg=(Sum(o)-Sum(altcoin))).annotate(tarct=Count(o))
            if gregor == "maximum":
                if sargh == "sentenceimprovement":
                    segtub = tublet.values(s).annotate(tAgg=(Max((si)))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(Max((si)))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(Max((si)))).annotate(tarct=Count(o))
                elif sargh == "sip":
                    segtub = tublet.values(s).annotate(tAgg=(Max(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(Max(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(Max(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                else:
                    segtub = tuble.values(s).annotate(tAgg=(Max((o)))).annotate(tarct=Count(o))
                    segnub = nuble.values(s).annotate(nAgg=(Max((o)))).annotate(tarct=Count(o))
                    overall = overall.values(s).annotate(oAgg=(Max((o)))).annotate(tarct=Count(o))
            if gregor == "minimum":
                if sargh == "sentenceimprovement":
                    segtub = tublet.values(s).annotate(tAgg=(Min(si))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(Min(si))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(Min(si))).annotate(tarct=Count(o))
                elif sargh == "sip":
                    segtub = tublet.values(s).annotate(tAgg=(Min(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(Min(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(Min(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                else:
                    segtub = tuble.values(s).annotate(tAgg=(Min(o))).annotate(tarct=Count(o))
                    segnub = nuble.values(s).annotate(nAgg=(Min(o))).annotate(tarct=Count(o))
                    overall = overall.values(s).annotate(oAgg=(Min(o))).annotate(tarct=Count(o))
            if gregor == "standev":
                if sargh == "sentenceimprovement":
                    segtub = tublet.values(s).annotate(tAgg=(StdDev(si))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(StdDev(si))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(StdDev(si))).annotate(tarct=Count(o))
                elif sargh == "sip":
                    segtub = tublet.values(s).annotate(tAgg=(StdDev(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                    segnub = nublet.values(s).annotate(nAgg=(StdDev(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                    overall = overallet.values(s).annotate(oAgg=(StdDev(si/F('rangelow')+0.0))).annotate(tarct=Count(o))
                else:
                    segtub = tuble.values(s).annotate(tAgg=(StdDev(o))).annotate(tarct=Count(o))
                    segnub = nuble.values(s).annotate(nAgg=(StdDev(o))).annotate(tarct=Count(o))
                    overall = overall.values(s).annotate(oAgg=(StdDev(o))).annotate(tarct=Count(o))
    else:
        s = None
    return render(request, 'blog/test_filter.html',{'stitling': stitling, 'segtct': segtct, 'segnct': segnct, 'overct': overct, 'gregor': gregor,'simpallct': simpallct, 'simpleavect': simpleavect, 'simpall': simpall, 'simpleave': simpleave, 'otitle': otitle, 'ntitle': ntitle, 'overall': overall, 'segnub': segnub,'tuble': tuble,'segtub': segtub, 'title': title, 's': s})


# one parameter named request
def profile_upload(request):
    # declaring template
    template = "blog/profile_upload.html"
    data = DFrame.objects.all()
# prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address, phone, profile',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = DFrame.objects.update_or_create(
            num=column[0],
            filename=column[1],
            location=column[2],
            lastname=column[3],
            firstmiddle=column[4],
            casenumber=column[5],
            judge=column[6],
            psrwriter=column[7],
            prosecuter=column[8],
            attorney=column[9],
            closingauthor=column[10],
            statue=column[11],
            pleatype=column[12],
            unfiled924c=column[13],
            rangelow=column[14],
            rangehigh=column[15],
            mandatoryminimummonths=column[16],
            sentenceimposed=column[17],
            supervisedrelease=column[18],
            probation=column[19],
            cooperationreductionpercentage=column[20],
            courtrejectedinitialbindingplea=column[21],
            pretrialrelease=column[22],
            appealwaiver=column[23],
            restitution=column[24],
            plantoappeal=column[25],
            motionsfiled=column[26],
            motionswon=column[27],
            psrobjectionsfiled=column[28],
            psrobjectionswon=column[29],
            sentencingmemofiled=column[30],
            cooperation=column[31],
            chargebargainaffectingsentencing=column[32],
            variance=column[33],
            criminalhistorycategory=column[34],
            cctostate=column[35],
            cctofederal=column[36],
            mandatoryminimumimposed=column[37],
            adjustedoffenselevel=column[38] if column[38] else None,
            eightfiveone=column[39],
            ninetwofoure=column[40],
            fourbonepointone=column[41],
            expertemployed=column[42],
            investigatorinterviewedwitness=column[43],
            courtfollowedrecommendationofnonbindingpleaagreement=column[44],
            clientvisits=column[45],
            closingdate=column[46],
            special=column[47],
            caselength=column[48],
            formversion=column[49],
            mf=column[50]
        )
    context = {}
    return render(request, template, context)





#def index(request):
#    print("hello")
#    return(HttpResponse('something'))

#def post_list(request):
#    posts = Post.objects.all().order_by('published_date')
#    print(posts.first().text)
#    return render(request,'blog/post_list.html',{'posts': posts})

#def post_detail(request, pk):
#    post = get_object_or_404(Post,pk=pk)
#    return render(request,'blog/post_detail.html',{'post': post})

#def post_new(request):
#    if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm()
#    return render(request, 'blog/post_edit.html', {'form': form})

#def post_edit(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if request.method == "POST":
#        form = PostForm(request.POST, instance=post)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm(instance=post)
#    return render(request, 'blog/post_edit.html', {'form': form})
