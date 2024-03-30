'''
Websiteblocker
Created by: Jude Darmanin (darmanin1312@gmail.com)
Date: 10 June 2020
Version 2.0: 13 August 2023

This program is a website blocker. Websites to block include specified txt list of sites other custom sites specified below.

Script alters hosts.txt Windows file, which provides a mapping between a host name and an IP address. The script maps the banned sites back to the local address, effectively preventing the site from sending its own IP response.

To check if script is working use cmd:
    ping -n 1 #SITE to check received IP address
'''
import os
import re
import time
from pyuac import main_requires_admin

# ***DEFINING INITIAL VARIABLES***

hosts = r"C:\Windows\System32\drivers\etc\hosts" #---> PATH OF HOSTS.TXT FILE
local = "127.0.0.1"
end_delay = 180 #delay execution of ban end by this amount of seconds


# ***DEFINE BLOCKLIST***

blocklist = []

#add custom sites
custom = [] #custom sites to add to blocklist (e.g. www.facebook.com)
for site in custom:
    blocklist.append(site)

#add sites from predefined txt list
blocklist = r'' #---> SPECIFY PATH TO TXT FILE CONTAINING LIST OF SITES
if os.path.exists(blocklist):
    with open(blocklist, 'r') as f:
        for site in f.readlines():
            if site.startswith('EXC_'):
                s = re.sub('EXC_', '', site)
                blocklist.append(s.rstrip('\n'))
            else: 
                s = re.sub('www.', '', site)
                blocklist.append(s.rstrip('\n'))

# ***IMPLEMENTING BAN***

def block_sites(blocklist, local = local, hosts = hosts, end = False):
    '''
    Block websites in 'blocklist' by redirecting URL to 'local' host via 'hosts' file.
    Set end=True to remove blocked sites and return 'hosts' to original state.
    '''
        
    #add sites to block
    if not end:
        with open(hosts, "a+") as file: #open for appending (to end of file) and reading
            content=file.read()
            file.write("\n")
            for site in set(blocklist):
                if site not in content:
                    file.write(local+" "+site+"\n")
     
    #when ban ends, delete lines blocking websites but keep the remaining lines.
    else:
        with open(hosts, "r+") as file: #open for reading and writing
            lines = file.readlines() 
            file.seek(0) #return cursor to start of screen
            for item in lines: 
                if (not any(site in item for site in blocklist) and not item.isspace()): #for every line in the file, check whether any website in blocklist is present or whether line is empty space.
                    file.write(item) 
            file.truncate() #reduces file size to current pointer position (last line after writing)


# ***RUNNING***

@main_requires_admin #since hosts file requires admin permission
def main():
    '''
    Run program with admin permission.
    '''
    prompt = input('Enter \'y\' if you wish to end ban, else ban will exectute ')

    if prompt.lower() == 'y':
        print(f'\nBan will end in {end_delay} seconds. Press CTRL+C to cancel...')
        time.sleep(end_delay)
        block_sites(blocklist, end = True)
    else:
        block_sites(blocklist, end = False)


if __name__ == "__main__":
    main()