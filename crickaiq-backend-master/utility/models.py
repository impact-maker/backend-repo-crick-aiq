from django.db import models
from account.models import User
from master.models import Country


def prediction_banner_picture_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/prediction_picture/{1}'.format(instance.pk, filename)

class Prediction(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="PredictionUser")
    country_b = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE, related_name="PredictionUser")
    format = models.CharField(max_length=255, null=True, blank=True)
    match_date = models.DateField(null=True, blank=True)
    banner_picture = models.ImageField(upload_to=prediction_banner_picture_directory_path, height_field=None,
                                width_field=None, max_length=100, verbose_name="BannerPicture", null=True, blank=True)
    result = models.JSONField(null=True, blank=True)
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"

    status = models.CharField(choices=Status.choices, default=Status.ACTIVE, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Match vs {self.country_b.longName} on {self.match_date}'


class Analysis(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="AnalysisUser")
    result = models.JSONField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.name} created {self.type} analysis'