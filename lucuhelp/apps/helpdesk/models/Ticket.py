import imaplib
from django.db import models


class Ticket(models.Model):
    STATUS_OPEN = 1
    STATUS_PENDING = 2
    STATUS_REOPENED = 3
    STATUS_SOLVED = 4
    CHOICE_STATUS = (
        (STATUS_OPEN, u'Abierto'),
        (STATUS_PENDING, u'En espera'),
        (STATUS_REOPENED, u'Re Abierto'),
        (STATUS_SOLVED, u'Resuelto'),
    )

    PRIORITY_LOW = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_HIGH = 3
    PRIORITY_URGENT = 4
    CHOICE_PRIORITY = (
        (PRIORITY_LOW, u'Bajo'),
        (PRIORITY_MEDIUM, u'Medio'),
        (PRIORITY_HIGH, u'Re Alto'),
        (PRIORITY_URGENT, u'Urgente'),
    )

    client = models.ForeignKey(
        'Client',
        related_name='ticket_set',
    )

    subject = models.CharField(
        max_length=45
    )

    description = models.TextField()

    status = models.SmallIntegerField(
        choices=CHOICE_STATUS,
        default=STATUS_OPEN
    )

    priority = models.SmallIntegerField(
        choices=CHOICE_PRIORITY,
        default=PRIORITY_LOW
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        editable=False,
        auto_now=True
    )

    def __unicode__(self):
        return self.subject

    class Meta:
        app_label = 'helpdesk'


class TicketDetail(models.Model):

    ticket = models.ForeignKey(
        'Ticket',
        related_name='ticket_detail_set',
    )

    employee = models.ForeignKey(
        'Employee',
        related_name='ticket_detail_set',
    )

    description = models.TextField()

    reply = models.BooleanField(
        default=False
    )
    
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        editable=False,
        auto_now=True
    )

    def __unicode__(self):
        return self.subject

    class Meta:
        app_label = 'helpdesk'