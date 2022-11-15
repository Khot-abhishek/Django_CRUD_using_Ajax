from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentRegistration
from .models import User

# Create your views here.
def home(request):
    context = {
        'form':StudentRegistration(),
        'students': User.objects.all()
    }
    return render(request, 'enroll/home.html', context)

def save_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        
        if form.is_valid():
            
            id = request.POST.get('stu_id')
            print('id: ', id )
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
    # create new record or update existing based on presence of "ID"        
            if(id == " "):
                student = User(name=name, email=email, password=password)
            else:
                student = User(id=id, name=name, email=email, password=password)
            student.save()
            
    # queryset objects cannot be json sirealized so it is converted to a list inside context
            all_users = list( User.objects.values() )   # <-----
            context = {
                'msg':'form saved successfully',
                'students': all_users        
            }
            return JsonResponse(context, )
        else:
            all_users = list( User.objects.values())
            context = {
                'msg':'Unable to save Form',
                'students': all_users
            }
            return JsonResponse(context)


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('del_id')
        user = User.objects.get(pk=id)
        user.delete()
        return JsonResponse({'status':1})
    return JsonResponse({'status':0})


# view to populate the form fields when edit button is clicked
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('edit_id')
        student = User.objects.get(pk=id)
        student_data = {'id':student.id, 'name':student.name, 'email':student.email, 'password':student.password}
        return JsonResponse(student_data)