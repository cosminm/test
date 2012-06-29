from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType



class CommonInfo(models.Model):
    nume = models.CharField(max_length=100)
    nume_utilizator = models.CharField(max_length=100)
    parola = models.CharField(max_length=20, blank=True)
    adresa_domiciliu = models.CharField(max_length=200)
    adresa_corespondenta = models.CharField(max_length=200, blank=True)
    telefon = models.CharField(max_length=20, blank=True)

    class Meta:
        abstract = True
        ordering = ['nume']
        app_label = "cms" 

    def __unicode__(self):
        return self.nume



class Clasa(models.Model):
    nume = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Clase"
        app_label = "cms" 

    def __unicode__(self):
        return self.nume



class Student(CommonInfo):
    clasa = models.ForeignKey(Clasa, blank=True)

    class Meta:
        verbose_name_plural = "Studenti"
        permissions = (
            ("edit", "Can edit own data"),
            ("view", "Can view anything"),
        )

    def save(self, force_insert=False, force_update=False, using=None):
        super(Student, self).save(force_insert=False,
                                    force_update=False,
                                    using=None)
        user = User.objects.create_user(self.nume_utilizator,
                                        self.adresa_corespondenta,
                                        self.parola)

#        content_t = ContentType.objects.get(app_label='cms', model='student')

#        permission = Permission.objects.create(codename='edit',
#                                               name='Can edit own data',
#                                               content_type=content_t)
#        user_permissions.add(permission)

#        permission = Permission.objects.create(codename='view',
#                                               name='Can view anything',
#                                               content_type=content_t)
#        user_permissions.add(permission)



class Profesor(CommonInfo):
    clasa = models.ManyToManyField(Clasa, blank=True)

    class Meta:
        verbose_name_plural = "Profesori"
        permissions = (
            ("edit", "Can edit own data"),
            ("view", "Can view anything"),
            ("add", "Can add new students"),
            ("assign", "Can assign students to their own classes"),
        )


    def save(self, force_insert=False, force_update=False, using=None):
        super(Profesor, self).save(force_insert=False,
                                    force_update=False,
                                    using=None)
        user = User.objects.create_user(self.nume_utilizator,
                                        self.adresa_corespondenta,
                                        self.parola)

#        content_type = ContentType.objects.get(app_label='cms', model='Profesor')

#        permission = Permission.objects.create(codename='edit',
#                                               name='Can edit own data',
#                                               content_type=content_type)
#        user_permissions.add(permission)

#        permission = Permission.objects.create(codename='view',
#                                               name='Can view anything',
#                                               content_type=content_type)
#        user_permissions.add(permission)

#        permission = Permission.objects.create(codename='add',
#                                               name='Can add new students',
#                                               content_type=content_type)
#        user_permissions.add(permission)

#        permission = Permission.objects.create(codename='assign',
#                                               name='Can assign students to their own classes',
#                                               content_type=content_type)
#        user_permissions.add(permission)



