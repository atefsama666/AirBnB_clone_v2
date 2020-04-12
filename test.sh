#!/bin/bash
# nginx quick simple setup
if [[ -z $(dpkg -l | grep "nginx") ]]; then
	apt-get -y update
	apt-get -y install nginx
fi