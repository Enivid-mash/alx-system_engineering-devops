# This module increases the number of concurrent connections that an Nginx server
# can handle by modifying the open file limit in the Nginx configuration.

# Define a module for Nginx concurrency management
module nginx_concurrency (
  # Optional: Add parameters here if needed
) {

  # Document the class (recommended)
  @doc {
    type    => Module
    author  => 'YOU (your name or organization)'
    summary => 'Manages Nginx worker processes for increased concurrency'
  }

  # Define a file resource to modify the open file limit in /etc/default/nginx
  file { '/etc/default/nginx':
    ensure  => present,
    owner   => root,
    group   => root,
    mode    => '0644',

    # Use `replace` to ensure specific line is modified
    replace => {
      'worker_processes 15;' => 'worker_processes 4096;',
    }
  }

  # Define a service resource to restart Nginx after the configuration change
  service { 'nginx' :
    ensure          => running,
    enable          => true,
    restart_command => '/sbin/service nginx restart',  # Adjust path if needed
  }

  # Notify the service resource about changes to the file resource
  notify <<| EoNotify |
    Service['nginx']
  EoNotify
}

