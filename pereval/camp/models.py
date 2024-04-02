from django.db import models


class Tourist(models.Model):
    email = models.EmailField(max_length=128, unique=True)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)


class Pereval(models.Model):
    NEW ='NW'
    PENDING ='PN'
    ACCEPTED ='AC'
    REJECTED ='RJ'
    STATUS_CHOICES = (
        ('NW', 'new'),
        ('PN', 'pending'),
        ('AC', 'accepted'),
        ('RJ', 'rejected'),
    )
    a_1 = '1A'
    a_2 = '2A'
    a_3 = '3A'
    a_4 = '4A'
    LEVEL_CHOICES = (
        ('1A', '1A'),
        ('2A', '2A'),
        ('3A', '3A'),
        ('4A', '4A')
    )
    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.OneToOneField('Coords', on_delete=models.CASCADE)
    tourist_id = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)
    winter_lev = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=a_1)
    spring_lev = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=a_1)
    summer_lev = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=a_1)
    autumn_lev = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=a_1)


class Coords(models.Model):
    latitude = models.DecimalField(decimal_places=8, max_digits=10)
    longitude = models.DecimalField(decimal_places=8, max_digits=10)
    height = models.IntegerField(default=0)


class Images(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=128)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.title




