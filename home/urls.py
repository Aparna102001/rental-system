from django.urls import path
from . import views
urlpatterns = [
     path('',views.index,name='index'),
     path('userhome/',views.userhome,name='userhome'),
     path('signin/',views.signin,name='signin'),
     path('register/',views.register,name='register'),
     path('agency/',views.agency,name='agency'),
     path('travel/',views.travel,name='travel'),
     path('vehiclebooking/',views.vehiclebooking,name='vehiclebooking'),
     path('vehicle_selection/',views.vehicleselection,name='vehicle_selection'),
     path('homepage/',views.homepage,name='homepage'),
     path('profile/',views.profile,name='profile'),
     path('travelinfo/',views.travelinfo,name='travelinfo'),
     path('agentregister/',views.agentregister,name='agentregister'),
     path('agentsignin/',views.agentsignin,name='agentsignin'),
     path('vehicleslot/<int:slot_id>/',views.vehicleslot,name='vehicleslot'),
     #path('vehicle_details/',views.vehicleselection,name='vehicle_selection'),
     #path('vehicle_details/', views.display_vehicle_details, name='select_vehicle'),
     #path('vehicle_selection/', views.display_vehicle_selection, name='vehicle'),
     path('vehicle-selection/', views.vehicle_selection, name='vehicle_selection'),
     path('confirmation/', views.confirmation_details, name='confirmation_details'),

     #path('booking_confirm/',views.booking_confirm,name='booking_confirm')
]