#!/usr/bin/env bash
#time: 11/7/17
#!/bin/bash
echo "${1}/bin/elasticsearch -p ${2}/es.pid" -d | su - elasticsearch