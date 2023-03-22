from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    location_filter_choices = [
        ('temple_bar', 'Temple Bar'),
        ('sandymount', 'Sandymount'),
        ('rathmines', 'Rathmines'),
        ('portobello', 'Portobello'),
        ('ballsbridge', 'Ballsbridge'),
        ('dublin_docklands', 'Dublin Docklands'),
        ('smithfield', 'Smithfield'),
        ('cabra', 'Cabra'),
        ('ashtown', 'Ashtown'),
        ('phibsborough', 'Phibsborough')
    ]

    RATE_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Fair'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    price = models.TextField(max_length=50, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    content = models.TextField(blank=True)
    location = models.TextField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    location_filter = models.CharField(
        max_length=32, choices=location_filter_choices, default='none'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
