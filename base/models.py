from django.db import models

# Department model
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Course model
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Purpose model
class Purpose(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Material model
class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Profile model
class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material)

    def __str__(self):
        return self.name
