# HeroViredNetworkingAssignment

# Git: https://github.com/Mahi2k/HeroViredNetworkingAssignment

Question 1 : For 10 Points
Deploy a website on localhost using either apache2 or nginx. Create a DNS name for this website as ‘awesomevicky.com’. You can use any web template you want or can write your own simple html code. Write a detailed documentation with steps involved.

# STEPS #
 
1# Update apt package manager
	> sudo apt-get update

2# Install NGINX in the system
	> sudo apt-get install nginx

3# Check the default configuration of NGINX (it should be inside /etc/nginx/sites-available/).   
  Check the text inside deafult config file by triggering the command
	> sudo cat deafult

4# Create a config file for awesomevicky.com use command
	> cd /etc/nginx/sites-available/
	> sudo nano awesomevicky.com

	# Paste below config settings inside the file
	server {
        listen 80;
        root /var/www/html/awesomevicky.com;
        index index.html index.htm;
        server_name awesomevicky.com;
        location / {
                try_files $uri $uri/ =404;
        }
    }

5# Create a symbolic link for this config file from sites-available to sites-enabled folder by using the command
	> ln -s /etc/nginx/sites-available/awesomevicky.com /etc/nginx/sites-enabled/

6# Till now we have created a config for the domain name now we need to create a website with the same folder name and index.html file inside it
	> cd /var/www/html
	> sudo mkdir awesomevicky.com
    > sudo chown -R www-data:www-data /var/www/html/awesomevicky.com #This provides permission to read and write the files in folder
	> cd awesomevicky.com/
	> sudo nano index.html
	
7# Add below html code in index.html file and save it
	<html>
        <head>
	        <title>AWESOME VICKY SERVER</title>
        </head>
        <body>
            <section>
                <h1>Welcome to Environment NGNIX SERVER</h1>
                <p>This is the first example for creating NGINX SERVER</p>
            </section>
        </body>
    </html>

8# Restart the nginx server
    > sudo systemctl restart nginx

9# Still website with domain name will not work since we have not added a DNS entry
    # In windows we have to add an entry in the host file for redirecting the website domain to localhost web server. It is present inside "c:/windows/system32/driver/etc/"
    > Add entry as below 
        127.0.0.1	awesomevicky.com
        ::1         awesomevicky.com

10# After saving this file go to chrome and hit the domain "awesomevicky.com"

11# Voila..!! Website is working.


# Git: https://github.com/Mahi2k/HeroViredNetworkingAssignment

Question 2 : For 10 Points
A website can have many subdomains and different services are running on them. Write a Python script to check the status of the subdomains which are up or down. The script should automatically check the status every min and should update it in tabular format on the screen. Write a detailed documentation of it. 

# STEPS #

1# Update apt package manager
	> sudo apt-get update

2# Install NGINX in the system
	> sudo apt-get install nginx

3# Check the default configuration of NGINX (it should be inside /etc/nginx/sites-available/).   
  Check the text inside deafult config file by triggering the command
	> sudo cat deafult

4# Create a config file for awesomevicky.com use command
	> cd /etc/nginx/sites-available/
	> sudo nano awesomevicky.com

	# Paste below config settings inside the file
	server {
        listen 80;
        root /var/www/html/awesomevicky.com;
        index index.html index.htm;
        server_name awesomevicky.com;
        location / {
                try_files $uri $uri/ =404;
        }
    }

5# Create a symbolic link for this config file from sites-available to sites-enabled folder by using the command
	> ln -s /etc/nginx/sites-available/awesomevicky.com /etc/nginx/sites-enabled/

6# Till now we have created a config for the domain name now we need to create a website with the same folder name and index.html file inside it
	> cd /var/www/html
	> sudo mkdir awesomevicky.com
	> cd awesomevicky.com/
	> sudo nano index.html
	
7# Add below html code in index.html file and save it
	<html>
        <head>
	        <title>AWESOME VICKY SERVER</title>
        </head>
        <body>
            <section>
                <h1>Welcome to Environment NGNIX SERVER</h1>
                <p>This is the first example for creating NGINX SERVER</p>
            </section>
        </body>
    </html>

8# Restart the nginx server
    > sudo systemctl restart nginx

9# Still website with domain name will not work since we have not added a DNS entry
    # In windows we have to add an entry in the "host" file for redirecting the website domain to "localhost" web server. It's present inside "c:/windows/system32/driver/etc/"
    > Add entry as below 
        127.0.0.1	awesomevicky.com
        ::1         awesomevicky.com

10# After saving this file go to chrome and hit the domain "awesomevicky.com"

11# Viola..!! Website is working.

12# Follow steps from 4 to 10 for making a subdomains
    > dev.awesomevicky.com
    > qa.awesomevicky.com

13# Create a python script that will monitor the domain and subdomain and will print the status every minute on the console
    > We can easily do it using http library that will hit the webservers and check the status codes in a while loop
    > Also we will use a python library called as urllib
    > Use utility as time for time intervals
    > Created a file called as scanner.py



    # Git: https://github.com/Mahi2k/HeroViredNetworkingAssignment

1. Download VirtualBox for windows 
2. Download UBUNTU Virtual Disc Image to a folder (I used kali linux)
3. Open Oracle Virtual box manager
4. Click on NEW (*) sign given in the UI to add a new Virtual Machine
4. Add Name of the server
5. Check if resources allocated to virtual machine is proper and up to the mark.
6. Add the UBUNTU Virtual disc image to the virtual machine, also select type and version as Linux and Ubuntu(64 Bit) respectively
7. Provide base memory as 4096 mb and 2 cpu to the in ahrdware section, click on finish
8. Your newly created virtual machine should come in the list, select and hit start button.
9. Wait for some time and your virtual machine will appear in a new window.
10. Now as per assignmnet we need to install nginx and host a website, for the sake of time I hosted default website
11. 1# Update apt package manager
	> sudo apt-get update

    2# Install NGINX in the system
        > sudo apt-get install nginx

    3# Check the default configuration of NGINX (it should be inside /etc/nginx/sites-available/).   
    Check the text inside deafult config file by triggering the command
        > sudo cat deafult

    4# Create a config file for awesomevicky.com use command
        > cd /etc/nginx/sites-available/
        > sudo nano awesomevicky.com

        # Paste below config settings inside the file
        server {
            listen 80;
            root /var/www/html/awesomevicky.com;
            index index.html index.htm;
            server_name awesomevicky.com;
            location / {
                    try_files $uri $uri/ =404;
            }
        }

    5# Create a symbolic link for this config file from sites-available to sites-enabled folder by using the command
        > ln -s /etc/nginx/sites-available/awesomevicky.com /etc/nginx/sites-enabled/

    6# Restart the nginx server
    > sudo systemctl restart nginx

12. Now come to host machine and open NMAP
13. Scan the port that you just started with nginx in virtual machine.
14. Observe the Open ports