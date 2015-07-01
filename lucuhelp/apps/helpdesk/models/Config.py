from django.db import models
import base64


class Config(models.Model):

    email = models.EmailField(
        max_length=45
    )

    password = models.CharField(
        max_length=45
    )

    hostname = models.CharField(
        max_length=45
    )

    directory = models.CharField(
        max_length=45
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        editable=False,
        auto_now=True
    )
    
    def set_password(self, password):
        self.password = base64.b64encode(password)
    
    def get_password(self):
        return base64.b64decode(self.password)

    def __unicode__(self):
        return self.email

    class Meta:
        app_label = 'helpdesk'