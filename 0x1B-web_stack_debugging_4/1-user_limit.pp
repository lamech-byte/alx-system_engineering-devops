exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 50000',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  user    => 'holberton',
}
