from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Register,Agency,bookdetails,Vehicle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Agent_Register,Agency
from .models import Vehicle
from .forms import Travel_view

def index(request):
    return render(request,'index.html')
def userhome(request):
    return render(request,'userhome.html')

def register(request):
    if request.method=='POST':
        
        username=request.POST.get('username')
        
        email=request.POST.get('em')
        
        password=request.POST.get('password')
        
        user=Register.objects.create(username=username,email=email,password=password)
        user.save()
        
        return redirect('signin')
    else:
        messages.error(request,"account creation unsuccessfull")
    return render(request,'register.html')



def signin(request):
     if request.method=='POST':
        
        username=request.POST.get('username')
        
        password=request.POST.get('password')
        
        user=Register.objects.filter(username=username,password=password).exists()
        print(user,'ok')
        if user is True:
            return redirect('userhome')    
     else:
         
         messages.error(request,"userid or password is error")
     return render(request,'signin.html')

def profile(request):
    return render(request,'profile.html')
total_passengers=[]
def travel(request):
    if request.method=='POST':
        print(',,,,,,,,,,,,,,,,,,,,,,,,,')
        oneway=request.POST.get('oneway')
        
        roundtrip=request.POST.get('roundtrip')
        fro=request.POST.get('fro')
        
        to=request.POST.get('to')
        date1=request.POST.get('date1')
        
        date2=request.POST.get('date2')
        pickup=request.POST.get('pickup')
        
        #dropoff=request.POST.get('dropoff')
        kid=request.POST.get('kid')
        print(kid,'llllllllllllllll')
        adult=request.POST.get('adult')
        print(adult,'llllllllllllllll')
        senior=request.POST.get('senior')
        print(senior,'llllllllllllllll')
        # calculate passengers count
        total=int(kid)+int(adult)+int(senior)
        total_passengers.append(total)
        print(total,'KKKKKKKKKKKKKKKKKKKKKKKKKK')
        #calculate fare
        details=bookdetails.objects.create(date1=date1,date2=date2,pickup=pickup,fro=fro,to=to)
        details.save()
        #details=bookdetails.objects.get(id=details_id)

       
        
        return redirect('vehiclebooking')
    return render(request,'travel.html')



        


def agency(request):
    elements = Agency.objects.all()
    return render(request,'agency.html',{'elements':elements})
def vehicleselection(request):
    return render(request, 'vehicle_selection.html')   

def vehiclebooking(request):
    print('oops')
    
    for i in total_passengers:
        passengers_count=i
        print(passengers_count,'lllllllllllllllllllllllllllll')
    
    if  passengers_count <= 6:
        a=Vehicle.objects.filter(type='car')
        print(a,'bv')
    elif passengers_count >6 and passengers_count <=22:
        a=Vehicle.objects.filter(type='traveller')
        print(a,'bv')
    else:
        a=Vehicle.objects.filter(type='bus')
        print(a,'bv')
        return redirect('vehicle_selection')
        #return render(request, 'vehicle_selection.html')
    return render(request, 'vehiclebooking.html',{'key':a})
#def booking_confirm(request):
    #return render(request, 'booking_confirm.html')
    #return render(request, 'vehiclebooking.html' )
    


#def vehicleslot(request):
    #vslots = Vehicle.objects.filter(available=True).order_by('name','number','driver','type','fare')
    #context = {'vslots': vslots}
    #return render(request, 'vehicleslot.html', context)  

def homepage(request):
    return render(request,'homepage.html')
def travelinfo(request):
    if request.method=='POST':
      form = Travel_view(request.POST,request.FILES)
      if form.is_valid():
            form.save()
            return redirect('homepage')
           #return render(request,'homepage.html')
        
    else:
        messages.error(request,"seems like there is an error")
        form = Travel_view()
        return render(request,'travelinfo.html')

def profile(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        
        mobile=request.POST.get('mobile')
        
        address=request.POST.get('address')
        location=request.POST.get('location')
        id_number=request.POST.get('id_number')
        
        
        user=Agency.objects.create(name=name,mobile=mobile,address=address,location=location,id_number=id_number)
        user.save()
        
        return redirect('homepage')
    else:
        messages.error(request,"Vehicle adding unsuccessfully")
    return render(request,'profile.html')
def agentregister(request):
    if request.method=='POST':
        
        username=request.POST.get('username')
        
        email=request.POST.get('em')
        
        password=request.POST.get('password')
        
        user=Agent_Register.objects.create(username=username,email=email,password=password)
        user.save()
        
        return redirect('agentsignin')
    else:
        messages.error(request,"account creation unsuccessfull")
    return render(request,'agentregister.html')
def agentsignin(request):
     if request.method=='POST':
        
        username=request.POST.get('username')
        
        password=request.POST.get('password')
        
        user=Agent_Register.objects.filter(username=username,password=password).exists()
        print(user,'ok')
        if user is True:
            return redirect('homepage')    
     else:
         
         messages.error(request,"userid or password is error")
     return render(request,'agentsignin.html')


def vehicleslot(request, slot_id):
    vslots = Vehicle.objects.get(id=slot_id)
    print(vslots)
    #if request.method == 'POST':
    vslots.available = True
    vslots.save()
    #return redirect('vehicleslot/<int:slot_id>/')
    #context = {'vslots': vslots}
    #return render(request, 'vehicleslot.html')
    return render(request, 'vehicleslot.html', {'vslots': vslots})  

#def vehicleselection(request):
    
    #return render(request, 'vehicle_details.html') 
#def display_vehicle_selection(request):
    #vehicles = Vehicle.objects.all()  # Query all vehicles from the database
    #return render(request, 'vehicle_selection.html', {'vehicles': vehicles})
#def display_vehicle_details(request):
    
    #if request.method == 'POST':
        #selected_name = request.POST.get('selected_name', '') 
        #print(selected_name) # Retrieve the selected name from the form
        #try:
            #vehicle = Vehicle.objects.get(name=selected_name)
            #return render(request, 'vehicle_details.html', {'vehicle': vehicle})
        #except Vehicle.DoesNotExist:
           # error_message = f"No vehicle with the name '{selected_name}' found."
            #return render(request, 'error.html', {'error_message': error_message})
    #else:
        #vehicles = Vehicle.objects.all()  # Query all vehicles from the database
        #return render(request, 'vehicle_selection.html', {'vehicles': vehicles})
from django.shortcuts import render, get_object_or_404
def vehicle_selection(request):
    if request.method == 'POST':
        selected_name = request.POST.get('selected_name', None)
        if selected_name:
            vehicle = get_object_or_404(Vehicle, name=selected_name)
            return render(request, 'confirmation_details.html', {'vehicle': vehicle})

    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_selection.html', {'vehicles': vehicles})      

def confirmation_details(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'confirmation_details.html', {'vehicle': vehicle})