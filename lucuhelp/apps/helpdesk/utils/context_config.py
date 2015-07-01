from apps.helpdesk.models.Config import Config


def server_config(request):
    config = Config.objects.all().first()
    return {'config': config }