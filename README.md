# Pass&Py CL
Pass&Py CL is an account authentication program that runs in the command line.
## Features
**Two-Factor Authentication** (via email) - requires a numerical code that is sent to your email before logging into your account. Can be four to ten digits long.<br/>
**Passcode** - a second numerical password which is required when logging into your account. Can be 4 or 6 digits long.
**Account Key** a six digit number which is used in case of a security restriction.<br/>
**Security Lock** - an account state which is enabled when suspicious activity is recognised on your account. In this account state, you cannot modify any account settings. You will need your account key to restore your account.<br/>
**Admin Tools** - with admin tools, if you have an account with administrative privileges enabled, you can ban, lock, and grant administrative privileges to other users.<br/>
## Before You Use Pass&Py
You will need to download and install the latest version of Python from https://www.python.org/downloads/release/python-383/.
We recommend you don't use Pass&Py CL with older versions of Python.
## How To Use Pass&Py CL
On your Terminal, type ```python``` and drag the **Pass&Py.py** onto the command line.<br/><br/>
**IMPORTANT:** On Windows, you need to add Python to the Windows Path. A tutorial on how to do this can be found here: https://datatofish.com/add-python-to-windows-path/<br/><br/>
![CommandLineHelp](https://s7.gifyu.com/images/CommandLineHelp.gif)<br/><br/>
To register for an account, type ```/register [first name] [surname] [username] [email] [phone] [password] [confirm password]```.<br/>
To login to your account, type ```/login [username or email] [password]```<br/>
For more commands, do ```/help``` while Pass&Py CL is running.<br/>

**IMPORTANT:** For Two-Factor Authentication to work, you will need to edit the script and enter your own email credentials. You will then have to enter a SMTP Server and SMTP Port. You can find a list of servers and ports for popular email providers below.<br/>

**Gmail**<br/>
SMTP Server: smtp.gmail.com<br/>
SMTP Port: 587<br/><br/>
**Outlook**<br/>
SMTP Server: smtp.office365.com<br/>
SMTP Port: 587<br/><br/>
**Yahoo**<br/>
SMTP Server: smtp.mail.yahoo.com<br/>
SMTP Port: 465 or 587<br/><br/>

If your email provider wasn't listed, you can look for it here: https://www.smtpsoftware.com/smtp-server-list/


