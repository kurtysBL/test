from email.policy import default
from pyexpat import model
from django.db import models
from account.models import User
from django_quill.fields import QuillField


# Create your models here.
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True
        
        
class Cathegorie(Timestamp):
    nom = models.CharField(max_length = 50)
    description = models.TextField(max_length = 500)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'cathegorie'
    
    
    def __str__(self):
        return self.nom

class Article(Timestamp):
    titre  =  models.CharField(max_length = 50)
    contenu =  QuillField()
    description1 = models.TextField(max_length = 1000, null= True, blank = True)
    description2 = models.TextField(max_length = 1000, null= True, blank = True)
    description3 = models.TextField(max_length = 1000, null= True, blank = True)
    cathegorie =  models.ForeignKey(Cathegorie, on_delete = models.CASCADE, related_name = 'articles')
    published = models.BooleanField(default = False)
    author = author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'articles')
    image = models.ImageField(upload_to = 'blog/images', null= True, blank = True)
    video = models.FileField(upload_to= 'blog/videos', null=True, blank=True)
    liste = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'post'
    
    
    def __str__(self):
        return self.titre
    
    # Test de l'editor QUILL (django-quill-editor)
    
    
