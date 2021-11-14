from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect


from .forms import ContactForm
from .models import ContactId


def home_page(request):
    contacts = ContactId.objects.all()
    form = ContactForm()
    if request.is_ajax():
        new = ContactForm(request.POST)
        if new.is_valid():
            new.save()
            return JsonResponse({}, status=200)
        else:
            errors = new.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    return render(request, 'bookapp/home.html', context={'contacts': contacts, 'form': form})


def edit(request, pk):
    obj = get_object_or_404(ContactId, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.modified_contact()
            return redirect('/')
    else:
        form = ContactForm(instance=obj)
    return render(request, 'bookapp/contact.html', {'form': form})
