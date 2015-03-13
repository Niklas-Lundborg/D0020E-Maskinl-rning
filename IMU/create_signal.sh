#!/bin/bash

# Fetch signal from IMU and save in txt file, data.txt

# Specs
usb='/dev/ttyUSB0'
baud='9600'
file='data.txt'

gnome-terminal --tab -e "gtkterm -p $usb -s $baud" & cat $usb >> $file
