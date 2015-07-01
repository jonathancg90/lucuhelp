from django.core.management.base import BaseCommand
from optparse import make_option

from apps.helpdesk.models.Client import Client
from apps.helpdesk.models.Category import Category
from apps.helpdesk.models.Employee import Employee
from apps.helpdesk.models.Config import Config


class Command(BaseCommand):
    data_delete = False

    option_list = BaseCommand.option_list + (
        make_option('--delete',
                    action='store_true',
                    dest='delete',
                    default=False,
                    help='Delete data'),
    )

    def handle(self, *args, **options):
        entity = args[0]

        if options['delete']:
            self.data_delete = True

        if entity == 'test_data':
            if self.data_delete:
                Client.objects.all().delete()
                Category.objects.all().delete()
                Employee.objects.all().delete()
                Config.objects.all().delete()
            else:
                self.insert_client()
                self.insert_category()
                self.insert_employee()
                self.insert_config()

    def insert_client(self):
        client = Client()
        client.name = 'Condor Travel'
        client.quota = 40
        client.email = 'javier@condortravel.com'
        client.save()
        
        client = Client()
        client.email = 'web@elcomercio.com'
        client.quota = 30
        client.name = 'El Comercio'
        client.save()

        client = Client()
        client.email = 'web@elcomercio.com'
        client.quota = 50
        client.name = 'El Comercio'
        client.save()

    def insert_category(self):
        category = Category()
        category.name = 'Servidor'
        category.save()

        category = Category()
        category.name = 'Estilos'
        category.save()

        category = Category()
        category.name = 'Otros'
        category.save()

        category = Category()
        category.name = 'Otros'
        category.save()

    def insert_employee(self):
        employee = Employee()
        employee = Employee()
        
    def insert_config(self):
        config = Config()
        config.email = 'admin@sublimart.pe'
        config.hostname = 'prince.superdnssite.com'
        config.directory = 'Inbox'
        config.set_password('admin')
        config.save()