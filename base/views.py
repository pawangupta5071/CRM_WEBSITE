from django.shortcuts import render,HttpResponse,redirect
from .models import Contact,Deal,Company,Task,Customer
from .forms import ContactForm,DealForm,CompanyForm,TaskForm

# Create your views here.
def home(request):
    deals = Deal.objects.all()
    customers = Contact.objects.all()
    contacts_count = Contact.objects.all().count()
    companies_count = Company.objects.all().count()
    tasks_count = Task.objects.all().count()
    deals_count = Deal.objects.all().count()
    context = {
        "deals": deals,
        "customers":customers,
        "contacts_count": contacts_count,
        "companies_count": companies_count,
        "tasks_count": tasks_count,
        "deals_count": deals_count,
               }
    return render(request,"base/home.html",context)

def contact_list(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    return render(request,"base/contact_list.html",context)
    
def contact_detail(request,pk):
    contact = Contact.objects.get(pk=pk)
    context = {'contact':contact}
    return render(request,"base/contact_detail.html",context)

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'base/contact_form.html', {'form': form})


def contact_edit(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail',pk=pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'base/contact_form.html',{'form':form})



def company_list(request):
    companies = Company.objects.all()
    context = {'companies':companies}
    return render(request, 'base/company_list.html',context)
    
def company_detail(request,pk):
    company = Company.objects.get(pk=pk)
    context = {'company':company}
    return render(request, 'base/company_detail.html',context)

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(request.POST)
    return render(request, 'base/company_form.html',{'form': form})

def company_edit(request,pk):
    company = Company.objects.get(pk=pk)
    if request.method =='POST':
        form = CompanyForm(request.POST,instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_detail',pk=pk)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'base/company_form.html',{'form': form})


def deal_list(request):
    deals = Deal.objects.all()
    context = {"deals":deals}
    return render(request, "base/deal_list.html",context)
    
def deal_detail(request,pk):
    deal = Deal.objects.get(pk=pk)
    context = {"deal":deal}
    return render(request, "base/deal_detail.html",context)


def deal_create(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deal_list')
    else:
        form = DealForm()
    return render(request, "base/deal_form.html",{'form': form})


def deal_edit(request,pk):
    deal = Deal.objects.get(pk=pk)
    if request.method == 'POST':
        form = DealForm(request.POST,instance=deal)
        if form.is_valid():
            form.save()
            return redirect('deal_detail',pk=pk)
    else:
        form = DealForm(instance=deal)
    return render(request, "base/deal_form.html",{'form': form})


def task_list(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request,"base/task_list.html",context)
    
def task_detail(request,pk):
    task = Task.objects.get(pk=pk)
    context = {"task":task}
    return render(request,"base/task_detail.html",context)

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,"base/task_form.html",{'form': form})

def task_edit(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail',pk=pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'base/task_form.html', {'form':form})