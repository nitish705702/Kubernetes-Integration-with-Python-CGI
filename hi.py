
#!/user/bin/python3

import cgi
#import subprocess
import time
from datetime import datetime

print("content-type: text/html")
print()

fi=cgi.FieldStorage()
cmd=fi.getvalue("x")
from subprocess import getoutput
print("<h2>Your Command is:=</h2>",cmd,"<h2>\n Output is :-</h2>")
print("<h3>Today's date and Time is (:%Y-%n-%d %H:%H)</h3>",format(datetime.now()))
print(subprocess.getoutput("kubctl "+(cmd)+" ---kubeconfig admin.conf")
print("x"+100)
print()
print(output)
print()
print("x"*100)
time.sleep(0)
print('<h1 style="background-color: green">Thank You for using this kubernates UI Page</h1>')
