#!/bin/bash
#Basic Python Scripts: This script is used to evaluate the value of a string. This snippet of code can be used to match input password from user and either grant access or deny access using if statements
#Zakia Ben Youss Gironda

read -e -sp "Enter Password : " secret_pass; 
if [ "$secret_pass" == "password" ]; then
# change password to the password you want to use

printf "Correct Password, you are logged in/n"
else 
printf "Incorrect Password, exiting.. "
fi
exit 1

