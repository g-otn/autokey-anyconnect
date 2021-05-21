#!/bin/bash

if ! pgrep "autokey" > /dev/null
then
    echo "Starting AutoKey...";
    autokey > /dev/null 2>&1 &
    sleep 0.5 # Needs to be enough for autokey to start, so we can use autokey-run
fi

autokey-run -s disconnect-vpnui

#if pgrep "autokey" > /dev/null
#then
#    echo "Killing AutoKey...";
#    kill $(ps aux | grep '/usr/bin/autokey' | awk '{print $2}') 
#fi

