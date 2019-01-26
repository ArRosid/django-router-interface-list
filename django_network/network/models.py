from django.db import models


NAPALM_MAPPING = {
    'cisco_ios': 'ios',
    'cisco_iosxe': 'ios'
}

class Device(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=70)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    device_type = models.CharField(max_length=100, choices=(('router', 'Router'),('switch', 'Switch')), blank=True)
    platform = models.CharField(max_length=100, choices=(('cisco_ios', 'Cisco IOS'),('cisco_iosxe', 'Cisco IOS XE')), blank=True)

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)

    @property
    def napalm_driver(self):
        return NAPALM_MAPPING[self.platform]