#!/bin/bash 
# Basic Python Script: This script asks user to input a number then it uses the while loop to display the ascending order of numbers starting from the user first input minimum increasing by 1 to the unser input maximum 
# Zakia Ben Youss Gironda
echo -n "Enter the number you want to count up from MIN: "
read countmin
echo -n "Enter the number you want to count up to MAX: "
read countmax
while [[ countmin -le countmax ]]; do  
echo "$countmin"
countmin=$((countmin + 1)) 
done
echo "Finished counting"
