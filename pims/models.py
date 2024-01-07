from django.db import models

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"
    

class ProjectInfo(models.Model):
    project_Name = models.CharField(max_length=200, verbose_name = "Project Name")
    catagory = models.ForeignKey (Catagory, on_delete=models.SET_NULL, null=True)
    zone = models.CharField(max_length=20)
    woreda = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places = 2,max_digits = 100 )
    Rebate = models.DecimalField(decimal_places = 2,max_digits = 100, verbose_name = "Rebate in Percent")
    consultant = models.CharField(max_length=20)
    startDate = models.DateTimeField(verbose_name = 'Start Date')
    endDate = models.DateTimeField( verbose_name =" End Date")
    update= models.DateField(auto_now=True)
    def __str__(self):
        return self.project_Name
    
    
    
  

    


              

    

    @property
    def Vat (self):
        vat =self.price * 15/100
        return (vat)
    def AfterVat (self):
        return(self.price - self.Vat)
    @property
    def Remaining (self):
        return(self.price - self.payed)
   
    @property
    def afterRebate (self):
        return(self.price - self.rebate)
