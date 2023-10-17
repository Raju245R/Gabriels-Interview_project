from django.shortcuts import render,redirect
from django.contrib.postgres.search import *
from .models import Details
import base64
# Create your views here.
def view(request):  ### define function for rendering html page
    filter=request.GET.get("filter")  ### if we put value into the searchbox and it get then will operate.
    #sort=request.GET.get("sort")
    alpha=["ALL","A","B","C","D","E","F",
           "G","H","I","J","K","L","M",
           "N","O","P","Q","R","S","T",
           "U","V","W","X","Y","Z"] ### list declare for print alphabets using iteration 
    if filter in alpha:## if any value get by filter then it works
        if filter=="ALL":
            obj=Details.objects.all()
        else:
            obj=Details.objects.filter(username__contains=filter)
    else:### otherwise process
        if request.method == 'POST': ### post method also same as get method but differences between them that post method form inserted value that posted in this function  
            search=request.POST.get('search') ### variable declaration
            if len(search)>0: ## check condition
                obj=Details.objects.filter(username__contains=search.upper())
            else:
                obj=Details.objects.all() 
        else:
            obj=Details.objects.all()   
    primary_number=[] ## empty lists to store phone numbers seapartion
    secondary_number=[]
    img_list=[]### we included online url images also will accepted, so we can run given logic using this list 
    for i in obj:
        phone=i.userphone.split(",") ### phone numbers splited 
        if len(phone)==2:
            primary_number.append(phone[0]) ## phone numbers stored in the lists when act as seaparation
            secondary_number.append(phone[1])
        elif len(phone)==1:
            primary_number.append(phone[0]) ## if user can given only one number it will executed
            secondary_number.append(" ")
        else: ## otherwise
            primary_number.append(" ")
            secondary_number.append(" ")
        if i.userprofileimg: ### online url image doesn't acted convert binary, they pass directedly string data type
            if "https" in str(i.userprofileimg):
                link=str(i.userprofileimg).replace("b","",1)
                link=link.replace("'","") ### replace b and ' when online url link image comes to perform
                img_list.append(link) ### stored it
            else:
                i.userprofileimg=base64.b64encode(i.userprofileimg).decode('utf-8') ### local images converts binary using base64 module (--pip install pybase64 --)
                img_list.append("")
        else:
            img_file=open("C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/avatar.jpg","rb") ### default image set
            i.userprofileimg=base64.b64encode(img_file.read()).decode('utf-8') ### I did set that default image at local disk, so we converts binary
            img_list.append("")
    #### there are four lists returned
    det=zip(obj,primary_number,secondary_number,img_list) ### so we join four lists to single list using zip function
    return render(request,"view.html",{'det':det,'alpha':alpha})