#!/usr/bin/env bash
#time: 11/7/17
#!/bin/bash
su - elasticsearch <<EOF
${1}/bin/elasticsearch -p ${2}/es.pid -d
EOF