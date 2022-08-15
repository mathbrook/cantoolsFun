#! /usr/bin/bash
lsusb
read -p "what port is the candapter on " usbPort
sudo slcand -o -s8 -t hw -S 1000000 ttyUSB$usbPort
sudo ip link set up slcan0
candump slcan0 | python3 -m cantools decode ks5e.dbc