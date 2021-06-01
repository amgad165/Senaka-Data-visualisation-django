from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from adminsortable.models import SortableMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager ,Group,PermissionsMixin

class OrderEntry(models.Model):
    ACTT = models.CharField(verbose_name='ACTT#', max_length=100)
    ORDER = models.CharField(verbose_name='ORDER#', max_length=100)
    PO = models.CharField(verbose_name='PO#', max_length=100)
    TAG = models.CharField(verbose_name='TAG', max_length=100)
    F2INPUT= models.CharField(verbose_name='F2 INPUT', max_length=100)
    RUBBER = models.CharField(verbose_name='RUBBER', max_length=100)
    INSIDECOLOR = models.CharField(verbose_name='INSIDE COLOR#', max_length=100)
    OUTSIDECOLOR = models.CharField(verbose_name='OUTSIDE  COLOR#', max_length=100)
    INSIDECOLORDESC = models.CharField(verbose_name='INSIDE COLOR DESC', max_length=100)
    OUTSIDECOLORDESC = models.CharField(verbose_name='OUTSIDE COLOR DESC', max_length=100)
    LINEQTY = models.CharField(verbose_name='LINE QTY', max_length=100)
    OPENING = models.CharField(verbose_name='OPENING', max_length=100)
    OPENINGWIDTH = models.CharField(verbose_name='OPENINGWIDTH', max_length=100)
    OPENINGHT = models.CharField(verbose_name='OPENING HT', max_length=100)
    REINFORCEMENT = models.CharField(verbose_name='REINFORCEMENT', max_length=100)
    SPACER = models.CharField(verbose_name='SPACER#', max_length=100)
    OVERALLTHICKNESS = models.CharField(verbose_name='OVERALL THICKNESS', max_length=100)
    MULTIPOINTLOCK = models.CharField(verbose_name='MULTI POINT LOCK', max_length=100)
    WINDOWTYPE1ST = models.CharField(verbose_name='1ST WINDOW TYPE', max_length=100)
    WINDOWWIDTH1ST = models.CharField(verbose_name='1ST WINDOW WIDTH', max_length=100)
    WINDOWHT1ST = models.CharField(verbose_name='1ST WINDOW HT', max_length=100)
    WINDOWGLASS1ST = models.CharField(verbose_name='1ST WINDOW GLASS #', max_length=100)
    WINDOWTYPE2ND = models.CharField(verbose_name='2ND WINDOW TYPE', max_length=100)
    WINDOWWIDTH2ND = models.CharField(verbose_name='2ND WINDOW WIDTH', max_length=100)
    WINDOWHT2ND = models.CharField(verbose_name='2ND WINDOW HT', max_length=100)
    WINDOWGLASS2ND = models.CharField(verbose_name='2ND WINDOW GLASS #', max_length=100)
    WINDOWTYPE3RD = models.CharField(verbose_name='3RD WINDOW TYPE', max_length=100)
    WINDOWWIDTH3RD = models.CharField(verbose_name='3RD WINDOW WIDTH', max_length=100)
    WINDOWHT3RD = models.CharField(verbose_name='3RD WINDOW HT', max_length=100)
    WINDOWGLASS3RD = models.CharField(verbose_name='3RD WINDOW GLASS #', max_length=100)
    WINDOWTYPE4TH = models.CharField(verbose_name='4TH WINDOW TYPE', max_length=100)
    WINDOWWIDTH4TH = models.CharField(verbose_name='4TH WINDOW WIDTH', max_length=100)
    WINDOWHT4TH = models.CharField(verbose_name='4TH WINDOW HT', max_length=100)
    WINDOWGLASS4TH = models.CharField(verbose_name='4TH WINDOW GLASS #', max_length=100)
    WINDOWTYPE5TH = models.CharField(verbose_name='5TH WINDOW TYPE', max_length=100)
    WINDOWWIDTH5TH= models.CharField(verbose_name='5TH WINDOW WIDTH', max_length=100)
    WINDOWHT5TH = models.CharField(verbose_name='5TH WINDOW HT', max_length=100)
    WINDOWGLASS5TH = models.CharField(verbose_name='5TH WINDOW GLASS #', max_length=100)
    WINDOWTYPE6TH = models.CharField(verbose_name='6TH WINDOW TYPE', max_length=100)
    WINDOWWIDTH6TH = models.CharField(verbose_name='6TH WINDOW WIDTH', max_length=100)
    WINDOWHT6TH = models.CharField(verbose_name='6TH WINDOW HT', max_length=100)
    WINDOWGLASS6TH = models.CharField(verbose_name='6TH WINDOW GLASS #', max_length=100)
    WINDOWTYPE7TH = models.CharField(verbose_name='7TH WINDOW TYPE', max_length=100)
    WINDOWWIDTH7TH = models.CharField(verbose_name='7TH WINDOW WIDTH', max_length=100)
    WINDOWHT7TH = models.CharField(verbose_name='7TH WINDOW HT', max_length=100)
    WINDOWGLASS7TH = models.CharField(verbose_name='7TH WINDOW GLASS #', max_length=100)
    WINDOWTYPE8TH = models.CharField(verbose_name='8TH WINDOW TYPE', max_length=100)
    WINDOWWIDTH8TH = models.CharField(verbose_name='8TH WINDOW WIDTH', max_length=100)
    WINDOWHT8TH = models.CharField(verbose_name='8TH WINDOW HT', max_length=100)
    WINDOWGLASS8TH = models.CharField(verbose_name='8TH WINDOW GLASS #', max_length=100)
    WINDOWTYPE9TH = models.CharField(verbose_name='9TH WINDOW TYPE', max_length=100)
    WINDOWWIDTH9TH = models.CharField(verbose_name='9TH WINDOW WIDTH', max_length=100)
    WINDOWHT9TH = models.CharField(verbose_name='9TH WINDOW HT', max_length=100)
    WINDOWGLASS9TH = models.CharField(verbose_name='9TH WINDOW GLASS #', max_length=100)
    WINDOWTYPE10TH = models.CharField(verbose_name='10TH WINDOW TYPE', max_length=100)
    WINDOWWIDTH10TH = models.CharField(verbose_name='10TH WINDOW WIDTH', max_length=100)
    WINDOWHT10TH = models.CharField(verbose_name='10TH WINDOW HT', max_length=100)
    WINDOWGLASS10TH = models.CharField(verbose_name='10TH WINDOW GLASS #', max_length=100)
    WINDOWGRILL1ST = models.CharField(verbose_name='1ST WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG1ST = models.CharField(verbose_name='1ST WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL2ND = models.CharField(verbose_name='2ND WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG2ND = models.CharField(verbose_name='2ND WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL3RD = models.CharField(verbose_name='3RD WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG3RD = models.CharField(verbose_name='3RD WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL4TH = models.CharField(verbose_name='4TH WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG4TH = models.CharField(verbose_name='4TH WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL5TH = models.CharField(verbose_name='5TH WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG5TH = models.CharField(verbose_name='5TH WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL6TH = models.CharField(verbose_name='6TH WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG6TH = models.CharField(verbose_name='6TH WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL7TH = models.CharField(verbose_name='7TH WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG7TH = models.CharField(verbose_name='7TH WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL8TH = models.CharField(verbose_name='8TH WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG8TH = models.CharField(verbose_name='8TH WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL9TH = models.CharField(verbose_name='9TH WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG9TH = models.CharField(verbose_name='9TH WINDOW GRILL CONFIG ', max_length=100)
    WINDOWGRILL10TH = models.CharField(verbose_name='10TH WINDOW GRILL#', max_length=100)
    WINDOWGRILLCONFIG10TH = models.CharField(verbose_name='10TH WINDOW GRILL CONFIG ', max_length=100)
    OPTION1ST = models.CharField(verbose_name='1ST OPTION#', max_length=100)
    OPTION2ND= models.CharField(verbose_name='2ND OPTION#', max_length=100)
    OPTION3RD = models.CharField(verbose_name='3RD OPTION#', max_length=100)
    OPTION4TH = models.CharField(verbose_name='4RD OPTION# ', max_length=100)
    OPTION5TH = models.CharField(verbose_name='5TH OPTION#', max_length=100)
    OPTION6TH = models.CharField(verbose_name='6TH OPTION#', max_length=100)
    OPTION7TH = models.CharField(verbose_name='7TH OPTION#', max_length=100)
    OPTION8TH = models.CharField(verbose_name='8TH OPTION#', max_length=100)
    OPTION9TH = models.CharField(verbose_name='9TH OPTION#', max_length=100)
    OPTION10TH = models.CharField(verbose_name='10TH OPTION#', max_length=100)
    LINEREMARK = models.CharField(verbose_name='LINE REMARK', max_length=100)
    GLASSCOMMENT = models.CharField(verbose_name='GLASS COMMENT', max_length=100)
    DOOR = models.CharField(verbose_name='DOOR #', max_length=100)
    DOOROPTION = models.CharField(verbose_name='DOOR OPTION', max_length=100)
    OEUSER = models.CharField(verbose_name='OE USER', max_length=100)


class date_range(models.Model):
    start_date = models.CharField(verbose_name='Start Date', max_length=100)
    end_date = models.CharField(verbose_name='End Date', max_length=100)
    
class Settings(models.Model):
    cutting=models.IntegerField()
    weld_clean=models.IntegerField()
    shipping=models.IntegerField()
    pnt_receiving=models.IntegerField()
    VP_receiving=models.IntegerField()
    loading_days=models.IntegerField(default=14)

    class Meta:
        verbose_name=u"Setting"
class Exceptions(models.Model):
    urban_part = models.CharField(verbose_name='URBAN PART', max_length=100,null=True,blank=True)
    window_type = models.CharField(verbose_name='WINDOW TYPE', max_length=100,null=True,blank=True)


    class Meta:
        verbose_name=u"Exceptions"


class MyAccountManager(BaseUserManager):
    def create_user(self, name, username, email, phone, password):
        if not name:
            raise ValueError('Name is required')
        if not username:
            raise ValueError('Username is required')
        if not email:
            raise ValueError('Email is required')
        if not phone:
            raise ValueError('Phone number is required')
        if not password:
            raise ValueError('Password is required')

        user = self.model(
            name=name,
            username=username,
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, username, email, phone, password):
        user = self.create_user(
            name=name,
            username=username,
            email=self.normalize_email(email),
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(verbose_name='name', max_length=50)
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(verbose_name='phone', max_length=20, unique=True)
    password = models.CharField(verbose_name='password', max_length=255)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone', 'email']

    objects = MyAccountManager()

    def __str__(self):
        return self.name + ', ' + '@' + self.username

    def save(self, *args, **kwargs):
        super(Account,self).save(*args,**kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse('account_detail',
                       args=[self.pk, self.name, self.username])
