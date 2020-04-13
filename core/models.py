from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=20)
    tag_line = models.CharField(max_length=50)
    image = models.ImageField(upload_to="owner")

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="about",null=True,blank=True)
    tags = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    profile_image = models.ImageField(upload_to="testimonials")
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    testimonial = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    icon = models.ImageField(upload_to="service")
    name = models.CharField(max_length=20)
    short_desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    logo = models.ImageField(upload_to="client")
    name = models.CharField(max_length=30)
    link = models.URLField()

    def __str__(self):
        return self.name

class Funfact(models.Model):
    happy_clients = models.IntegerField()
    working_hours = models.IntegerField()
    awards_won = models.IntegerField()
    coffee_consumed = models.IntegerField()

class sociallink(models.Model):
    facebook = models.URLField(blank=True)
    google = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

class Education(models.Model):
    date = models.DateField(blank=True)
    course = models.CharField(max_length=255,blank=True)
    institution = models.CharField(max_length=255,blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.course

class Experience(models.Model):
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True,null=True)
    position = models.CharField(max_length=255,blank=True)
    company = models.CharField(max_length=255,blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('from_date',)

    def __str__(self):
        return self.company

class Resume(models.Model):
    experience = models.CharField(max_length=30,blank=True,null=True)
    resume = models.FileField(upload_to="resume")

class Skill(models.Model):
    skill = models.CharField(max_length=30)
    skill_level = models.CharField(max_length=30,choices=(
        ('skill-1','95%'),
        ('skill-2','90%'),
        ('skill-3', '85%'),
        ('skill-4', '80%'),
        ('skill-5', '75%'),
        ('skill-6', '70%'),
    ))

    def __str__(self):
        return self.skill


class Portfolio(models.Model):
    category = models.CharField(max_length=100,blank=True,null=True)
    project_name = models.CharField(max_length=30,blank=True,null=True)
    author = models.CharField(max_length=30,blank=True,null=True)
    link = models.URLField(blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    technology = models.CharField(max_length=100,blank=True,null=True)
    image_1 = models.ImageField(upload_to='portfolio',blank=True,null=True)
    image_2 = models.ImageField(upload_to='portfolio',blank=True,null=True)
    image_3 = models.ImageField(upload_to='portfolio',blank=True,null=True)
    video_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.project_name


class ContactDetail(models.Model):
    description = models.TextField(null=True,blank=True)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    freelance = models.CharField(max_length=10)

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

