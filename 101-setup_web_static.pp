# Configures a server with nginx adding a custom header
exec { 'apt-get -y update':
  provider  => 'shell',
}
-> package {'check':
  name => "nginx",
  ensure => present,
}
-> exec { 'Creating folders':
  provider  => 'shell',
  command   => "sudo mkdir -p /data/web_static/releases/test",
}
-> exec { 'Creating folders part 2':
  provider  => 'shell',
  command   => "sudo mkdir -p /data/web_static/shared",
}
-> exec { 'Adding simple index':
  provider  => 'shell',
  command   => "echo -e '<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' > /data/web_static/releases/test/index.html",
}
-> exec { 'Creating sym link':
  provider  => 'shell',
  command   => "sudo ln -sf /data/web_static/releases/test/ /data/web_static/current",
}
-> exec { 'Changing ownership':
  provider  => 'shell',
  command   => "sudo chown -R ubuntu:ubuntu /data/",
}
-> exec { 'Handling redirection':
  provider  => 'shell',
  command   => "sudo sed -i ' 25i \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-enabled/default",
}
-> exec { 'sudo service nginx restart':
  provider  => 'shell',
}
