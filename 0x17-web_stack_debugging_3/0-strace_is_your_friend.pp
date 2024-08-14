# A script that removes p from php in the wp-settings.php file that had 500 status-code.
$file_path = '/var/www/html/wp-settings.php'
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin','/usr/bin']
}
