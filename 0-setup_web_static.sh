#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Update package lists and install Nginx
apt-get update
apt-get install -y nginx

# Create directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create directories if they don't exist
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create or update symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership and group recursively
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Modify Nginx configuration
printf %s "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     add_header X-Served-By $HOSTNAME;
     root        /etc/nginx/html;
     index       index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

     location /redirect_me {
         return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ/;
     }

     error_page 404 /404.html;
     location = /404 {
         root /var/www/html;
         internal;
     }
}" > /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
