from django.db import models


class Client(models.Model):
    
    name = models.CharField(
        max_length=45
    )
    
    phone = models.CharField(
        max_length=45
    )
    
    email = models.EmailField(
        max_length=45
    )

    quota = models.IntegerField()
 
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        editable=False,
        auto_now=True
    )

    def __unicode__(self):
        return self.name

    @property
    def domain(self):
        domain = self.email.partition("@")
        domain = domain[len(domain)]
        return domain

    class Meta:
        app_label = 'helpdesk'