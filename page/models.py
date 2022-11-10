from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# foreign key is a field that is a primary key to another field
# models.PROTECT simply doesnt allow a user to delete the foreign key
class Category(models.Model):
    name = models.CharField(max_length= 100)
# string function to return as default (category)
    def __str__(self):
        return self.name
class Post(models.Model):
    #database model my manager  by default renders the data on homepage and 
    # default its set to published so only data that is set to published will be displayed
    class PostObjects(models.Manager):
        # we run PostObjects to GET this function running
        def get_queryset(self):
            return super().get_queryset().filter(status = 'published')

    #options for choices
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default =1)
    title = models.CharField(max_length= 100)
    excerpt = models.TextField(null = True)
    content = models.TextField()
    slug =models.SlugField(max_length=250, unique_for_date = 'published')
# provides a Url to the particular category 
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name = 'page_post'
    )
    #CASCADE when author/ user is deleted his posts are also deleted
    status = models.CharField(
        max_length=10, choices = options, default= 'published'
    )
    objects = models.Manager() # default manager
    postobject = PostObjects() #custom manager
     
     # how data should be displayed either ascending or descending
    class Meta:
        ordering = ('-published',)

    def __str__(self):
            return self.title