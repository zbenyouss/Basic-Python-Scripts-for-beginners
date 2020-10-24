#!/bin/bash
#Basic Python Script: This script asks for user input value and evaluates the input. The script determines if the input is integer or not, and if the input is an int it determines if it is positive or negative, even or odd.
# Zakia Ben Youss Gironda

echo -n "Enter a value > " 
read INT 
 if [[ "$INT" =~ ^-?[0-9]+$ ]]; then
if [ "$INT" -eq 0 ]; then
 echo "Input is zero."
 else 
if [ "$INT" -lt 0 ]; then
 echo "Input is negative." 
else
 echo "Input is positive."
 fi
 if [ $((INT % 2)) -eq 0 ]; then
 echo "Input is even."
 else
 echo "Input is odd."
fi
fi 
else
echo "Input is not an integer." >&2
exit 1
fi 
