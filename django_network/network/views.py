from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Device
from napalm import get_network_driver
from netmiko import ConnectHandler

def index(request):
    devices = Device.objects.all()
    context = {
        'devices' : devices
    }
    return render(request, 'base.html', context)

def device(request, device_id):
    device = Device.objects.get(id=device_id)

    if request.method == 'POST':
        interface_name = request.POST.get('interface_name')
        enable = request.POST.get('enable')
        print(enable)
        config_cmd = ['interface {}'.format(interface_name)]
        if enable == "True":
            config_cmd.append(' shutdown')
        else:
            config_cmd.append(' no shutdown')

        conn_params = {
            'ip': device.host,
            'username': device.username,
            'password': device.password,
            'device_type': device.platform
        }

        print(config_cmd)
        with ConnectHandler(**conn_params) as device_conn:
            device_conn.send_config_set(config_cmd)

        return redirect('/device/{}'.format(device.id))
    if request.method == 'GET':
        
        driver = get_network_driver(device.napalm_driver)
        with driver(device.host, device.username, device.password) as device_conn:
            interfaces = device_conn.get_interfaces()
        
        print(interfaces)

        context = {
            'device': device,
            'interfaces' : interfaces
        }
        return render(request, 'device.html', context)
