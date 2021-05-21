#!/bin/bash

if ! pgrep "autokey" > /dev/null
then
    echo "Starting AutoKey...";
    autokey > /dev/null 2>&1 &
    sleep 0.5 # Needs to be enough for autokey to start, so we can use autokey-run
fi


if ! pgrep "vpnui" > /dev/null
then
    echo "Starting VPN UI...";
    /opt/cisco/anyconnect/bin/vpnui > /dev/null 2>&1 &
fi

autokey-run -s connect-vpnui
