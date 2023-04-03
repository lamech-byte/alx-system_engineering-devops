# Automates the task of creating a custom
# HTTP header response, but with Puppet.

exec { 'add_header':
  command     => "/bin/echo 'add_header X-Served-By ${hostname};' >> /etc/nginx/nginx.conf",
  unless      => "grep -q 'add_header X-Served-By' /etc/nginx/nginx.conf",
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
  notify      => Service['nginx'],
}
