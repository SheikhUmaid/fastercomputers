from django.db import models

# Create your models here.




class Student(models.Model):
    sur_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField()
    # adhaar = models.ImageField()
    address1 =  models.CharField(default = (""), max_length=50)
    address2 = models.CharField(default = (""), max_length=50)
    Courses = models.CharField(default = (""), max_length=50)
    total_fees = models.IntegerField(default = 0)
    deposited_fees = models.IntegerField(default=0)
    pending_fees = models.IntegerField(default=0, editable=False)
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.id}, {self.first_name}"
    
    def save(self,*args,**kwargs):
        self.pending_fees = int(self.total_fees) - int(self.deposited_fees)
        print(self.deposited_fees)
        super(Student, self).save(*args,**kwargs)
    