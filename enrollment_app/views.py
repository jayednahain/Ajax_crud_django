from django.http import JsonResponse
from django.shortcuts import render
from .forms import UserRegestationForm
from enrollment_app.models import User
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def HomeView(request):
   form = UserRegestationForm()
   studen_data_obj=User.objects.all()
   return render(request,'home.html',{'form':form,'sutdent_data':studen_data_obj})

def save_data(request):
   print('check')

   if request.method == "POST":
      print('ehck 2')
      form = UserRegestationForm(request.POST)
      #studen_data_obj = User.objects.all()
      #print(studen_data_obj)
      s_id = request.POST.get('student_id')
      print(s_id)
      name = request.POST['name']
      email = request.POST['email']
      password = request.POST['password']

      if (s_id == ''):
         user = User(name=name,email=email,passowrd=password)
      else:
         user = User(id=s_id,name=name, email=email, passowrd=password)
      user.save()

      #retun the data from data base
      send_data = User.objects.values()
      #print(send_data)
      student_data =list(send_data)

      return JsonResponse({'status':'Save','student_data':student_data})
   else:
      return JsonResponse({'status':0})
def del_data(request):

   if request.method =="POST":
      id = request.POST.get('sid')
      print(id)
      find_id = User.objects.get(pk=id)
      find_id.delete()

      return JsonResponse({'status':1})
   else:
      return JsonResponse({'status':0})

def edit_data(request):
   if request.method =="POST":
      id = request.POST.get('sid')

      student_data = User.objects.get(pk=id)
      student_data_send={
         "id":student_data.id,
         "name":student_data.name,
         "email":student_data.email,
         "password":student_data.passowrd
      }
      return JsonResponse(student_data_send)
