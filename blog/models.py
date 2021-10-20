from django.conf import settings
from django.db import models
from django.utils import timezone

class InputField:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class DFrame(models.Model):
    filterable_fields={
        "num" : InputField("ID Number", "number"),
        "filename" : InputField("File Name", "text"),
        "location" : InputField("Office Location", "text"),
        "lastname" : InputField("Last Name", "text"),
        "firstmiddle" : InputField("First and Middle Names", "text"),
        "casenumber" : InputField("Case Number", "text"),
        "judge" : InputField("Judge", "text"),
        "psrwriter" : InputField("PSR Writer", "text"),
        "prosecuter" : InputField("Prosecutor", "text"),
        "attorney" : InputField("Attorney", "text"),
        "closingauthor" : InputField("Closing Author", "text"),
        "statue" : InputField("Statute", "text"),
        "pleatype" : InputField("Plea Type", "text"),
        "unfilled924c" : InputField("Unfilled 924c?", "text"),
        "rangelow" : InputField("Lowest Guidelines-suggested Sentence (in months)", "number"),
        "rangehigh" : InputField("Highest Guidelines-suggested Sentence (in months)", "number"),
        "mandatoryminimummonths" : InputField("Mandatory Minimum (in months)", "number"),
        "sentenceimposed" : InputField("Sentence Imposed", "number"),
        "supervisedrelease" : InputField("Supervised Release", "number"),
        "probation" : InputField("Probation", "number"),
        "cooperationreductionpercentage" : InputField("Cooperation Reduction Percentage", "number"),
        "courtrejectedinitialbindingplea" : InputField("Court Rejected Initial Binding Plea", "text"),
        "pretrialrelease" : InputField("Pre-trial Release", "text"),
        "appealwaiver" : InputField("Appeal Waiver", "text"),
        "restitution" : InputField("Restitution", "text"),
        "plantoappeal" : InputField("Plan to Appeal", "text"),
        "motionsfiled" : InputField("Motions Filed", "text"),
        "motionswon" : InputField("Motions Won", "text"),
        "psrobjectionsfiled" : InputField("PSR Objections Filed", "text"),
        "psrobjectionswon" : InputField("PSR Objections Won", "text"),
        "sentencingmemofiled" : InputField("Sentencing Memo Filed", "text"),
        "cooperation" : InputField("Cooperation", "text"),
        "chargebargainaffectingsentencing" : InputField("Charge Bargain Affecting Sentencing", "text"),
        "variance" : InputField("Variance Applied", "text"),
        "criminalhistorycategory" : InputField("Criminal History Category", "text"),
        "cctostate" : InputField("CC To State", "text"),
        "cctofederal" : InputField("CC To Federal", "text"),
        "mandatoryminimumimposed" : InputField("Mandatory Minimum Imposed?", "text"),
        "adjustedoffenselevel" : InputField("Adjusted Offense Level", "text"),
        "eightfiveone" : InputField("851", "text"),
        "ninetwofoure" : InputField("924c", "text"),
        "fourbonepointone" : InputField("4b1.1", "text"),
        "expertemployed" : InputField("Expert Employed?", "text"),
        "investigatorinterviewedwitness" : InputField("Investigator Interviewed Witness?", "text"),
        "courtfollowedrecommendationofnonbindingpleaagreement" : InputField("Court Followed Recommendation of Nonbinding Plea Agreement?", "text"),
        "clientvisits" : InputField("Client Visits", "number"),
        "closingdate" : InputField("Closing Date", "number"),
        "special" : InputField("Special", "text"),
        "caselength" : InputField("Case Length (in months)", "number"),
        "formversion" : InputField("Form Version", "text"),
        "mf" : InputField("MF", "text"),
    }
    num=models.IntegerField(null=True)
    filename=models.CharField(max_length=300)
    location=models.CharField(max_length=50)
    lastname=models.CharField(max_length=100)
    firstmiddle=models.CharField(max_length=150)
    casenumber=models.CharField(max_length=100)
    judge=models.CharField(max_length=100)
    psrwriter=models.CharField(max_length=200)
    prosecuter=models.CharField(max_length=200)
    attorney=models.CharField(max_length=200)
    closingauthor=models.CharField(max_length=200)
    statue=models.CharField(max_length=500)
    pleatype=models.CharField(max_length=100)
    unfiled924c=models.CharField(max_length=100)
    rangelow=models.IntegerField(blank=True,null=True)
    rangehigh=models.IntegerField(blank=True,null=True)
    mandatoryminimummonths=models.IntegerField(blank=True,null=True)
    sentenceimposed=models.IntegerField(blank=True,null=True)
    supervisedrelease=models.IntegerField(blank=True,null=True)
    probation=models.IntegerField(blank=True,null=True)
    cooperationreductionpercentage=models.IntegerField(blank=True,null=True)
    courtrejectedinitialbindingplea=models.CharField(max_length=50)
    pretrialrelease=models.CharField(max_length=100)
    appealwaiver=models.CharField(max_length=50)
    restitution=models.CharField(max_length=50)
    plantoappeal=models.CharField(max_length=50)
    motionsfiled=models.CharField(max_length=200)
    motionswon=models.CharField(max_length=200)
    psrobjectionsfiled=models.CharField(max_length=50)
    psrobjectionswon=models.CharField(max_length=50)
    sentencingmemofiled=models.CharField(max_length=50)
    cooperation=models.CharField(max_length=50)
    chargebargainaffectingsentencing=models.CharField(max_length=50)
    variance=models.CharField(max_length=50)
    criminalhistorycategory=models.CharField(max_length=50)
    cctostate=models.CharField(max_length=50)
    cctofederal=models.CharField(max_length=50)
    mandatoryminimumimposed=models.CharField(max_length=50)
    adjustedoffenselevel=models.IntegerField(blank=True,null=True)
    eightfiveone=models.CharField(max_length=50)
    ninetwofoure=models.CharField(max_length=50)
    fourbonepointone=models.CharField(max_length=50)
    expertemployed=models.CharField(max_length=50)
    investigatorinterviewedwitness=models.CharField(max_length=50)
    courtfollowedrecommendationofnonbindingpleaagreement=models.CharField(max_length=50)
    clientvisits=models.IntegerField(blank=True,null=True)
    closingdate=models.DateTimeField(blank=True,null=True)
    special=models.CharField(max_length=200)
    caselength=models.IntegerField(blank=True,null=True)
    formversion=models.CharField(max_length=50)
    mf=models.CharField(max_length=50)

    def __str__(self):
        return str(self.num)


#class Post(models.Model):
#    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#    created_date = models.DateTimeField(default=timezone.now)
#    published_date = models.DateTimeField(blank=True, null=True)

#def publish(self):
#    self.published_date=timezone.now()
#    self.save()
