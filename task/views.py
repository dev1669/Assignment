from django.shortcuts import render
from . models import Lead, Lead_fields, Followup

##### Creating rest framework

#from django.http import HttpResponse
#from django.shortcuts import get_object_or_404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from . serializers import LeadSerializer
#from rest_framework.decorators import api_view


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Lead
from . serializers import LeadSerializer



@api_view(['GET', 'PUT', 'POST','DELETE'])
def snippet_detail(request, name):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Lead.objects.get(contact_person_name=name)
    except Lead.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeadSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LeadSerializer(snippet, data=request.data)
        #data = {}
        if serializer.is_valid():
            serializer.save()
            #data['success'] = 'Update was successful'
            #return Response(data=data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = LeadSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
### View for rest API's.

# API to get data.
#@api_view(['GET',])
#def api_get_data(request):
    #try:
        #lead_list = Lead.objects.all()
    #except Lead.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
    #if request.method == 'GET':
        #serialize = LeadSerializer(lead_list, many=True)
        #return Response(serialize.data)





# Create your views here.
def home(request):

    options = Lead_fields.objects.all()
    return render(request,'firstpage.html',{'options':options})



def secondpage(request):

    if request.method == 'POST':
        lead_options = request.POST.getlist('lead_options') 
        start_date = request.POST['start_date']  
        end_date = request.POST['end_date']
    
    
    #lead_data = Lead.objects.values(*option_list)

    lead_data = Lead.objects.filter(last_follow_up_date__range=[start_date,end_date])
    

    #for i in lead_options:
        #print(i)

    return render(request,'secondpage.html',{'lead':lead_data,'lead_options':lead_options})