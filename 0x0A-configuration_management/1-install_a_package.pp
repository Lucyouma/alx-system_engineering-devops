#!/usr/bin/puppet apply

# Ensure pip is available with the correct Python version
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'], # Ensure pip is installed first
}
