## Elasticsearch

Ambari service for install and manageing Elasticsearch stack on HDP cluster

Note: there show the version of environment.

- Ambari Version: 2.4.1.0-22
- HDP Stack Version: 2.5
- Elasticsearch Version: 5.2.0
- JDK Version: 1.8.0_111

  [下载地址](https://www.elastic.co/downloads/past-releases)
#### There are some problems to be noted here

 * Elasticsearch's pid file unable :
    - pid_dir = config\['configurations']\['elastic-site']\['pid_dir']
    - #pid_file = format("{pid_dir}/es.pid")

   I'm defining it this way： pid_file = "/var/run/elasticsearch/es.pid"
#### Warning:
- After the Elasticsearch successfully,Wait a moment.
- The node.master values should be defined as \[ 1 or 0 ] in elastic-site configs.

#### Troubleshoot
If the elasticsearch start failed,modifity the configuration:

- vim /etc/security/limits.conf 
```
* soft nofile 65536
* hard nofile 131072
* soft nproc 2048
* hard nproc 4096
```
- vim /etc/security/limits.d/90-nproc.conf 
```
*      soft     nproc     2048
```
- vim /etc/sysctl.conf 
```
vm.max_map_count=655360
```
sysctl -p  <file>    (default  /etc/sysctl.conf)