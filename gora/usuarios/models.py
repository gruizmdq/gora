from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from empresas.models import Empresa

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, empresa=None, password=None):
        if not email:
            raise ValueError("Los usuarios tienen que tener email")
        if not first_name:
            raise ValueError("Los usuarios tienen que tener nombre")
        if not last_name:
            raise ValueError("Los usuarios tienen que tener apellido")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name, 
            last_name = last_name,
            empresa = empresa
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, empresa=None, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name, 
            empresa = empresa, 
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    date = models.DateTimeField(verbose_name="Fecha de registro", auto_now_add=True)
    first_name = models.CharField(verbose_name="Nombre", max_length=30)
    last_name = models.CharField(verbose_name="Apellido", max_length=30)
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.SET_NULL,
        verbose_name="Empresa:",
        default=1,
        blank=True, 
        null=True
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.last_name + " " + self.first_name + " - " + self.empresa.name

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True    