from django.db import models

# Create your models here.

class SignUp(models.Model):
    Institute_Name = models.CharField(max_length=50)
    Owner_Name = models.CharField(max_length=50)
    State = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=10)
    Email = models.EmailField()
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Username

class Courses(models.Model):
    Institute_Id = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Course_Name = models.CharField(max_length=100)
    Duration = models.CharField(max_length=3)
    Fee = models.CharField(max_length=10)
    Reg_amt = models.CharField(max_length=10)

    def __str__(self):
        return self.Course_Name


class Enquiry(models.Model):
    Institute_Id = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Date = models.CharField(max_length=15)
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=20)
    Reference = models.CharField(max_length=50)
    Enquired_For = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Admission(models.Model):
    Institute_Id = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Date = models.CharField(max_length=15)
    Name = models.CharField(max_length=50)
    F_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=30)
    Gender = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    DOB = models.CharField(max_length=20)
    Course_Name = models.CharField(max_length=30)
    Fee = models.CharField(max_length=20)
    Duration = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos")
    Identity = models.ImageField(upload_to="identity")

    def __str__(self):
        return self.Name

class Receipt(models.Model):
    Date = models.CharField(max_length=20)
    Name = models.CharField(max_length=30)
    Mobile = models.CharField(max_length=20)
    Amount = models.CharField(max_length=50)
    Course = models.CharField(max_length=30)
    Institute_Id = models.ForeignKey(SignUp, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
