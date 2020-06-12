# Pass&Py CL
Pass&Py CL is an account authentication program that runs in the command line.
## Features
**Two-Factor Authentication** (via email) - requires a numerical code that is sent to your email before logging into your account. Can be four to ten digits long.<br/>
**Passcode** - a secound numerical password which is required when logging into your account. Can be 4 or 6 digits long.
**Account Key** a six digit number which is used in case of a security restriction.<br/>
**Security Lock** - an account state which is enabled when suspicious activity is recognised on your account. In this account state, you cannot modify any account settings. You will need your account key to restore your account.<br/>
**Admin Tools** - with admin tools, if you have an account with administrative privileges enabled, you can ban, lock, and grant administrative privileges to other users.<br/>
## Before You Use Pass&Py
Yow will need to download and install the latest version of Python from https://www.python.org/downloads/release/python-383/.
We recommend you don't use Pass&Py CL with older versions of Python.
## How To Use Pass&Py CL
On your Terminal, type ```python``` and drag the **Pass&Py.py** onto the command line.<br/><br/>
**IMPORTANT:** On Windows, you need to add Python to the Windows Path. A tutorial on how to do this can be found here: https://datatofish.com/add-python-to-windows-path/<br/><br/>
![CommandLineHelp](https://s7.gifyu.com/images/CommandLineHelp.gif)<br/><br/>
To register for an account, type ```/register [firstname] [surname] [username] [email] [phone] [password] [confirm password]```.<br/>
To login to your account, type ```/login [username or email] [password]```<br/>
For more commands, do ```/commands``` while Pass&Py CL is running.<br/>

**Please Note:** On lines **96** and **97**, you will need to edit the script and enter your own email credientials.
