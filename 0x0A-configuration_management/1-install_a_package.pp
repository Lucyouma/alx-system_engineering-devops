#!/usr/bin/pup
# This code will install a specified version of flask (2.1.0)
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}

