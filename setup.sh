#!/bin/bash

echo "Running chmod on shell scripts..."
chmod +x vpnui/connect-vpnui.sh
chmod +x vpnui/disconnect-vpnui.sh

echo "Moving AutoKey and shell scripts to AutoKey folder..."
mkdir -p ~/.config/autokey/data/
mv vpnui ~/.config/autokey/data/vpnui

echo "Done!"

