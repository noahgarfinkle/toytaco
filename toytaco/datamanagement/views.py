from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset_Type
from django.template import loader

# Create your views here.
def index(request):
    assetTypesList = Asset_Type.objects.order_by('name')
    output = ','.join([a.name for a in assetTypesList])
    print(output)
    #return HttpResponse(output)
    template = loader.get_template('datamanagement/index.html')
    context = {
        'assetTypesList': assetTypesList,
    }
    return HttpResponse(template.render(context,request))

def detail(request, asset_type_id):
    try:
        asset_type = Asset_Type.objects.get(pk=asset_type_id)
    except Asset_Type.DoesNotExist:
        raise Http404("Asset type does not exist")
    return render(request,'/data/detail.html',{'asset_type_id':asset_type_id})

    #return HttpResponse("you're looking at question %s." % (asset_type_id))
