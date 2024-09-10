import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from master.models import Country


class UserManager(BaseUserManager):
    def create_user(self, username, name=None):
        if not username:
            raise ValueError("User must have username")
        if name is not None:
            user = self.model(
                username=username,
                name=name
            )
        else:
            user = self.model(
                username=username,
            )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password):
        user = self.create_user(
            username,
            name
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_role_user(self, username=None, password=None, role=None, name=None, email=None, mobile=None):
        user = self.create_user(
            username,
            name
        )
        if password is None:
            password = User.objects.make_random_password()
        user.set_password(password)

        user.role_id = role
        if email is not None:
            user.email = email
        if mobile is not None:
            user.mobile = mobile
        user.save(using=self._db)
        return user



class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255)
    role_name = models.CharField(max_length=255, null=True, blank=True)

    class RoleStatus(models.TextChoices):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"

    status = models.CharField(choices=RoleStatus.choices, default=RoleStatus.ACTIVE, max_length=255)

    def __str__(self):
        return f"{self.role}  {self.role_name}"

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name


def profile_picture_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/profile/{1}'.format(instance.pk, filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, verbose_name="Email", null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Name")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='UserCountry')
    current_years = models.IntegerField(default=2)

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"

    status = models.CharField(choices=Status.choices, default=Status.ACTIVE, max_length=255)
    # end of custom fields

    created_on = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to=profile_picture_directory_path, height_field=None,
                                width_field=None, max_length=100, verbose_name="Profile Picture", null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_staff