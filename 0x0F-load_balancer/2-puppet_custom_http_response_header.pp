# Automates the task of creating a custom
# HTTP header response, but with Puppet.

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create index file
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

# Configure custom HTTP response header
file { '/etc/nginx/sites-available/default':
  content => template('nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Enable default Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service when configuration changes
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
}
