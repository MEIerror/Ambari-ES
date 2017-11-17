#!/usr/bin/env python
"""
Elasticsearch  service params

"""

from resource_management import *
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions import format
config = Script.get_config()

pid_dir = config['configurations']['elastic-site']['pid_dir']
#pid_file = format("{pid_dir}/es.pid")
pid_file = "/var/run/elasticsearch/es.pid"