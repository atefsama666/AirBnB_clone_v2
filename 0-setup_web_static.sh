#!/bin/bash
# nginx quick simple setup
v=$(dpkg -l | grep "nginx")
if [[ -z $v ]]; then
	apt-get -y update
	apt-get -y upgrade
	apt-get -y install nginx
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
simplehtml="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
echo -e "$simplehtml" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
location="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"
sed -i " 25i $location" /etc/nginx/sites-enabled/default
service nginx restart

