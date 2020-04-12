# Configures a server with nginx adding a custom header
file_line {'Editing file':
  line      => '\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}',
  path      => './atef',
  #after    => undef,
  #ensure   => 'present',
  match    => "server {", # /.*match/
  #multiple => undef, # 'true' or 'false'
  #name     => undef,
  #replace  => true, # 'true' or 'false'
}