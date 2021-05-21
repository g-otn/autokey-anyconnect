# AutoKey AnyConnect
AutoKey scripts to automatically connect and disconnect to/from a VPN using AnyConnect.

## Notes
The scripts expects a few things:
- **"Start VPN when AnyConnect is started" preference is disabled in AnyConnect.**
- There's a default Group and User, so they're filled automatically by AnyConnect once it tries to connect. Logging in once manually and/or checking the `~/.anyconnect` file may help.
- That, after logging in, a banner (dialog with some info/warning) will pop up.
- There's no external change by the user in the current focus of fields/buttons/etc in the UI.

Tested with: 
- AutoKey 0.95.10
- Cisco AnyConnect Secure Mobility Client 4.9.05042

## Setup
1. Install AutoKey:
```bash
sudo apt-get install autokey-common autokey-gtk
```

2. Clone this repository:
```bash
git clone https://github.com/g-otn/autokey-anyconnect.git
cd autokey-anyconnect
```

3. Modify the `vpnui/connect-vpnui.py` file, inserting your password:
```python
STARTUP_TIME = 0.5
PASSWORD = "#############" # <-- Your VPN user password here
CONTACTING_TIME = 2
CONNECTION_TIMEOUT = 15
```

4. Run the `setup.sh` script. This will simply `chmod` the `.sh` files and move them and the AutoKey scripts to the AutoKey folder:
```bash
chmod +x setup.sh
./setup.sh
```

5. Set up some aliases for ease of use. If you use bash, you can append these lines at your `.bashrc`:
```bash
# AnyConnect Aliases
alias connect-vpnui='bash ~/.config/autokey/data/vpnui/connect-vpnui.sh'
alias disconnect-vpnui='bash ~/.config/autokey/data/vpnui/disconnect-vpnui.sh'
```

6. Use the aliases to run the scripts. Example:
```bash
# Make sure AnyConnect is closed or its initial focus has not been changed
# before running the script
connect-vpnui
```

The repository folder can now be deleted and the scripts will now be located at `~/.config/autokey/data/vpnui`.
