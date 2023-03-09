from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



    

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(null=True,blank=True)
    ###
    # address = models.TextField()

    def __str__(self):
        return self.name
    


class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.first_name
    

class Deal(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=000)
    status = models.CharField(max_length=100, choices=[
        ('new', 'New'),
        ('in progress', 'In Progress'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    ],null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ###
    # description = models.TextField()
    # value = models.DecimalField(max_digits=10, decimal_places=2)
    # stage = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE,null=True,blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,null=True, blank=True)
    status = models.CharField(max_length=100, choices=[
        ('new', 'New'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
        ('deferred', 'Deferred'),
    ],null=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ###
    # description = models.TextField()

    def __str__(self):
        return self.title


