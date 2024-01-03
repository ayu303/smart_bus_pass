from django.db import models

# Create your models here.

class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    name = name = models.CharField(max_length=30)
    e_sign = models.ImageField(upload_to='home/e_sign', default="" )

class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    fathername = models.CharField(max_length=30)
    college = models.ForeignKey(College,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    roll = models.PositiveIntegerField()
    course = models.CharField(max_length=30)
    aadhar_photo = models.ImageField(upload_to='home/aadhar_photo', default="" )
    aadhar_number = models.PositiveIntegerField()
    previous_pass = models.BooleanField(default=True)
    pass_number = models.CharField(max_length=30, default="")
    route_from = models.OneToOneField(Route,related_name='%(class)s_from_created',on_delete=models.CASCADE ,null=True )
    route_to = models.OneToOneField(Route,related_name='%(class)s_to_created',on_delete=models.CASCADE, null=True)
    verify_college = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='home/profile_photo', default="" )
    current_pass = models.BooleanField(default=False)
    valid_from = models.DateField(null=True)
    valid_to = models.DateField(null=True)
    price = models.PositiveIntegerField(null=True)
    verify_manager = models.BooleanField(default=False)

class Pass(models.Model):
    pass_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE , related_name='%(class)s_requests_created')
    college = models.ForeignKey(College,on_delete=models.CASCADE , related_name='%(class)s_requests_created' )
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE , related_name='%(class)s_requests_created')
    valid_from = models.DateField()
    valid_to = models.DateField()
    payment = models.BooleanField()
    pass_file = models.ImageField(upload_to='home/pass', default="" )

class AuthUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    type = models.SmallIntegerField()
    student_id = models.ForeignKey(Student,related_name='%(class)s_student',on_delete=models.CASCADE ,null=True )
    college_id = models.ForeignKey(College,related_name='%(class)s_college',on_delete=models.CASCADE ,null=True )
    manager_id = models.ForeignKey(Manager,related_name='%(class)s_manager',on_delete=models.CASCADE ,null=True )




