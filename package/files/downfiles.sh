#!/usr/bin/env bash
#time: 11/2/17


ES_URL=$1 #es下载地址
#HEAD_URL=$2 #head插件下载地址
#NODE_URL=$3
WORK_DIR=$2  #安装目录
ES_USER=$3

#WORK_DIR=/usr/local/lib/ambari-service
#CLUSTERNAME='es-81'
#NODENAME='adm'
#NETWORKHOST='192.168.1.81'
#HTTPPORT='9200'
if [ ! -d ${WORK_DIR} ]; then
    mkdir -p ${WORK_DIR}
fi

id ${ES_USER} &> /dev/null
if [ $? -ne 0 ]; then
    useradd ${ES_USER}
fi

wget -O ${WORK_DIR}/elasticsearch-5.2.0.tar.gz  $ES_URL
tar -zxf ${WORK_DIR}/elasticsearch-5.2.0.tar.gz -C ${WORK_DIR}
rm -fr ${WORK_DIR}/elasticsearch-5.2.0.tar.gz
chown ${ES_USER}:${ES_USER} ${WORK_DIR}/elasticsearch-5.2.0 -R
#wget -O ${WORK_DIR}/elasticsearch-head-master.zip $HEAD_URL
#wget -O ${WORK_DIR}/node-v6.11.4-linux-x64.tar $NODE_URL
#tar -xf ${WORK_DIR}/node-v6.11.4-linux-x64.tar
#unzip ${WORK_DIR}/elasticsearch-head-master.zip &> /dev/null



#sed 's/1024$/2048/' /etc/security/limits.d/90-nproc.conf && echo "WARNING:changed the /etc/security/limits.d/90-nproc.conf"
#echo '* soft nofile 65536
#* hard nofile 131072
#* soft nproc 2048
#* hard nproc 4096' >>  /etc/security/limits.conf && echo "WARNING:changed the  /etc/security/limits.conf"
#echo "vm.max_map_count = 655360" >>  /etc/sysctl.conf
#sysctl -p &> /dev/null
######################################################head-plugin:

#sed -i "/port:/i hostname: '0.0.0.0'," ${WORK_DIR}/elasticsearch-head-master/Gruntfile.js
#
#ln -s ${WORK_DIR}/node-v6.11.4-linux-x64/bin/node     /usr/local/sbin
#ln -s ${WORK_DIR}/node-v6.11.4-linux-x64/bin/npm      /usr/local/sbin
#
#npm config set registry https://registry.npm.taobao.org
#
#cd ${WORK_DIR}/node-v6.11.4-linux-x64/lib/node_modules/npm
#npm install –g grunt
#
#cd ${WORK_DIR}/elasticsearch-head-master
#npm install
#ln -s ${WORK_DIR}/elasticsearch-head-master/node_modules/grunt/bin/grunt /usr/local/sbin
#grunt server  &

#start es with the user of elasticsearch
#su - elasticsearch <<EOF
#${WORK_DIR}/elasticsearch-5.2.0/bin/elasticsearch &;
#EOF
