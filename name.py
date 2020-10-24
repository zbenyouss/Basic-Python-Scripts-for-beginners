#!/bin/bash 

#Basic Python Script: The script reads the keyboard input then displays it. It then asks to input passphrased within 5 seconds otherwise input times out. The passphrase is then displayed if input does not time out.
# Zakia Ben Youss Gironda
read -e -p "Please enter name? "  $USER
echo "Name Entered: '$REPLY'"

if read -t 5 -sp "Enter secret-pass " secret_pass; then echo -e "\nSecret passphrase = '$secret_pass'" 
else 
echo -e "\nInput timed out" >&2 
exit 1 
fi
