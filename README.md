# Website blocker
 amend Windows hosts.txt file to block websites

Created by: Jude Darmanin (darmanin1312@gmail.com)
Date: 10 June 2020
Version 2.0: 13 August 2023

This program is a website blocker. Websites to block include specified txt list of sites other custom sites specified below.

Script alters hosts.txt Windows file, which provides a mapping between a host name and an IP address. The script maps the banned sites back to the local address, effectively preventing the site from sending its own IP response.

To check if script is working use cmd:
    ping -n 1 #SITE to check received IP address