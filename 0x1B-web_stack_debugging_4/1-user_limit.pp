# This module enables the user 'holberton' to log in and open files without encountering limitations caused by insufficient file limits.

# Increase Hard File Limit for 'holberton' User

exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase Soft File Limit for 'holberton' User
# The soft limit is the enforced limit on the number of open files a user can have, typically set lower than the hard limit. 
# By increasing it to 50000, we allow the 'holberton' user to open more files before encountering limitations.

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

