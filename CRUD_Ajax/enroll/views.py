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
            form.save()
            all_users = User.objects.values()
    # queryset objects cannot be json sirealized so it is converted to a list inside context
            context = {
                'msg':'form saved successfully',
                'students': list(all_users)        # <-----
            }
            return JsonResponse(context, )
        else:
            all_users = User.objects.values()
            context = {
                'msg':'Unable to save Form',
                'students': list(all_users)
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