#!/bin/bash 
# Basic Python Script: This script asks user to input a number then it uses the while loop to display the descending order of numbers starting from the user input number to 1
# Zakia Ben Youss Gironda

echo -n "Enter value you want to count down from > " 
read count

while [[ "$count" -gt 0 ]]; do 
echo "$count" 
count=$((count - 1)) 
done
echo "Finished counting down"


