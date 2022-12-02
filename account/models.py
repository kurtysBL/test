from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class MyUserManager(BaseUserManager):
    """
    Personnalise le manager du model utilisateur afin que l'adresse mail
    que l'adresse mail soit l'unique identifiant d'authentification.
    """

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        """
        Le methode setdefault() returne la valeur de la clé passée en paramètre (si le clé existe dans le dictionnaire)
        Si la clé n'existe pas, elle la crée et l'assigne à la valeur passée en deuxième paramètre.
        """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        """ 
        On leve une exception si on essaie de créer un utilisateur 
        non super-admin avec la methode create_superuser.
        """
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        #Si tout est ok on crée notre super admin
        return self.create_user(email, password, **other_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    username=None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name','last_name')

    objects = MyUserManager()
    
    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email