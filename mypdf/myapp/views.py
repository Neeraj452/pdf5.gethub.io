from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import  FileSystemStorage
from .forms import BookForm
from .models import My_pdf
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def contact(request):
    return render(request,'myapp/contact.html')
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document'] # Here name="document" in input use to access the data from input tag
        fs= FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        context['url'] = fs.url(name)
    return render(request,'myapp/upload.html',context)

def book_list(request):
    books = My_pdf.objects.all()
    return render(request,'myapp/book_list.html',{'books':books })

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/upload_book.html', {
        'form': form
    })

def delete_book(request, pk):
    if request.method == 'POST':
        book = My_pdf.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')