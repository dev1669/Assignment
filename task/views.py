from django.shortcuts import render
from . models import Lead, Lead_fields, Followup

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