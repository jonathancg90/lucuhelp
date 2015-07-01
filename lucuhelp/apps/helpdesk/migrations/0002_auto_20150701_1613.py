# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('hostname', models.CharField(max_length=45)),
                ('directory', models.CharField(max_length=45)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('reply', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(related_name='ticket_detail_set', to='helpdesk.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='quota',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=45),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='client',
            field=models.ForeignKey(related_name='ticket_set', to='helpdesk.Client'),
        ),
        migrations.AddField(
            model_name='ticketdetail',
            name='ticket',
            field=models.ForeignKey(related_name='ticket_detail_set', to='helpdesk.Ticket'),
        ),
    ]
