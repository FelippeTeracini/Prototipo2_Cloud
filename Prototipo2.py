import openstack
import errno
import argparse
import os

from openstack.config import loader
import sys

openstack.enable_logging(True, stream=sys.stdout)
config = loader.OpenStackConfig()

def create_connection(auth_url, region, project_name, username, password, domain):

    return openstack.connect(
        auth_url=auth_url,
        project_name=project_name,
        username=username,
        password=password,
        region_name=region,
        user_domain_id=domain,
        app_name='examples',
        app_version='1.0',
    )

# CREATE SERVER

auth_url = 'http://192.168.0.20:5000/v3'
region = 'RegionOne'
project_name = 'admin'
username = 'Tera'
password = 'cloudw'
domain = '4fd914425397433ab4fb6d4e284cd87f'
conn = create_connection(auth_url, region, project_name,
                         username, password, domain)
server = conn.compute.create_server(
    name='tera_server', image_id='ead603a9-1e26-44f6-9098-1df82afe8586', flavor_id='a3be2810-7e8b-48c2-a314-139562171678',
    networks=[{"uuid": '9ce9c3aa-4c22-49eb-9939-327711daa2b4'}], key_name='TeraKeyOfficial')


# DELETE SERVER
conn.compute.delete_server(server)
