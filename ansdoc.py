#!/usr/bin/python36

import subprocess
import cgi
import cgitb
cgitb.enable()

print("content-type: text/html")
print("\n")


form = cgi.FieldStorage()
n = form.getvalue('n')

form = cgi.FieldStorage()
p = form.getvalue('p')


subprocess.getoutput("sudo ansible-playbook /var/www/cgi-bin/ansdoc.yml --extra-vars='n={} p={}'".format(n,p))

print("<br>")
print("<br>")
print(subprocess.getoutput("sudo docker exec {} '/usr/bin/xpra start --bind-tcp=0.0.0.0:3333 --html=on --start-child=vlc --systemd-run=no' ".format(n)))

print("<br>")
print("<br>")
print("<br> <br> ---------------------------------------------- To watch video click here <a href = 'http://192.168.43.46:{}' > CLICK HERE </a>".format(p))
print("------------------------------------------------------------")

