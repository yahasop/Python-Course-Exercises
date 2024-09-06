#!/usr/bin/env python3

import argparse
import subprocess

parser = argparse.ArgumentParser(description='Program to receive an option or several and display information about the Linux host')

#Arguments defined for short and long versions. The store true action enable them to not receiving arguments
parser.add_argument('-d', '--distro', action='store_true', help='Displays distro information of the Linux host')
parser.add_argument('-m', '--memory', action='store_true', help='Displays memory information of the Linux host')
parser.add_argument('-c', '--cpu', action='store_true', help='Displays cpu information of the Linux host')
parser.add_argument('-u', '--user', action='store_true', help='Displays user information of the Linux host')
parser.add_argument('-l', '--load', action='store_true', help='Displays load average information of the Linux host')
parser.add_argument('-i', '--ip', action='store_true', help='Displays IP address information of the Linux host')

args = parser.parse_args()

#This code block enables that all options can be passed once, instead of one by one
#The subprocess.run mehtod allows us to run commands on Linux host. The shell=True option is for passing full commands to the method
#The subprocess itself doesnt print a stdout so we need to set the option to pipe the subprocess output into stdout
#The result is a byte, not a string so we need to convert with decode to UTF-8 to transform it into a string
if args.distro:
    proc = subprocess.run(["grep PRETTY /etc/os-release | awk -F '=' '{print $NF}'"], stdout=subprocess.PIPE, shell=True)
    print(f"This Linux Distro is: {proc.stdout.decode('utf-8')}")
if args.memory:
    proc = subprocess.run(["free -h"], stdout=subprocess.PIPE, shell=True)
    print("INFORMATION ABOUT MEMORY USAGE:")
    print(proc.stdout.decode('utf-8'))
if args.cpu:
    proc = subprocess.run(["lscpu | grep CPU"], stdout=subprocess.PIPE, shell=True) 
    print("INFORMATION ABOUT CPU:")
    print(proc.stdout.decode('utf-8'))
if args.user:
    proc = subprocess.run(["whoami"], stdout=subprocess.PIPE, shell=True) 
    print(f"The current user is: {proc.stdout.decode('utf-8')}")
if args.load:
    proc = subprocess.run(["w | grep load"], stdout=subprocess.PIPE, shell=True)
    print("INFORMATION ABOUT LOAD AVERAGE AND UPTIME:")
    print(proc.stdout.decode('utf-8'))
if args.ip:
    proc = subprocess.run(["curl -s -4 ifconfig.me"], stdout=subprocess.PIPE, shell=True) 
    print(f"The current public IP of this server is: {proc.stdout.decode('utf-8')}")
