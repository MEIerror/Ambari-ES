#!/usr/bin/env python
"""
Elasticsearch Params configurations
"""

from resource_management import *
import os

# server configurations
config = Script.get_config()



elastic_user = config['configurations']['elastic-env']['elastic_user']
elastic_group = config['configurations']['elastic-env']['user_group']
work_dir = config['configurations']['elastic-env']['work_dir']
es_tar_url = config['configurations']['elastic-env']['es_tar_url']
head_zip_url = config['configurations']['elastic-env']['head_zip_url']
node_tar_url = config['configurations']['elastic-env']['node_tar_url']

path_data = config['configurations']['elastic-site']['path_data']
cluster_name = config['configurations']['elastic-site']['cluster_name']
node_name = config['configurations']['elastic-site']['node_name']
network_host = config['configurations']['elastic-site']['network_host']
http_port = config['configurations']['elastic-site']['http_port']
log_dir = config['configurations']['elastic-site']['log_dir']
pid_dir = config['configurations']['elastic-site']['pid_dir']
node_master = config['configurations']['elastic-site']['node.master']
discovery_zen_ping_unicast_hosts =  config['configurations']['elastic-site']['discovery.zen.ping.unicast.hosts']

elastic_dir = format("{work_dir}/elasticsearch-5.2.0")
elastic_conf = format("{work_dir}/elasticsearch-5.2.0/config/elasticsearch.yml")
elastic_home = format("{/home/{elastic_user}")

hostname = config['hostname']
java_home = config['hostLevelParams']['java_home']

service_packagedir = os.path.realpath(__file__).split('/scripts')[0]

elk_server_hosts = config['clusterHostInfo']['master_hosts']
if elk_server_hosts is not None and len(elk_server_hosts) > 0:
    elk_server_host = elk_server_hosts[0]
check_es = format(
    'curl -k -s -o /dev/null -w "%{{http_code}}" http://{elk_server_host}:{http_port} |grep 200')

#java_home = config['configurations']['el-env']['java_home']