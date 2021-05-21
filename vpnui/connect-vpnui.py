import time

# ==============================================================================

STARTUP_TIME = 0.5          # Needs to be enough for the window to pop up
PASSWORD = "#############"  # Your password here
CONTACTING_TIME = 2         # Needs to be enough for connecting
CONNECTION_TIMEOUT = 15     # Needs to be enough for connecting after inputting group/username/password

# ==============================================================================

#system.exec_command("/opt/cisco/anyconnect/bin/vpnui", False)
#time.sleep(1)

# Wait for AutoKey / VPN UI to start
time.sleep(STARTUP_TIME)

# Focus VPN UI window
window.activate("Cisco AnyConnect Secure Mobility Client")
time.sleep(0.2)

# Navigate to Connect button
keyboard.send_key("<tab>") # Host list button
time.sleep(0.1)
keyboard.send_key("<tab>") # Config button
time.sleep(0.1)
keyboard.send_key("<tab>") # Connect button
time.sleep(0.1)

# Click Connect button
keyboard.send_key("<enter>")

# Wait until host is contacted and Group/Username is filled
time.sleep(CONTACTING_TIME)

# Expects password to be focused

# Type password
keyboard.send_keys(PASSWORD)
time.sleep(0.1)

# Click Connect button
keyboard.send_key("<enter>")
time.sleep(0.1)

# Wait for banner dialog to appear
window.wait_for_exist("Cisco AnyConnect - Banner", CONNECTION_TIMEOUT)
window.activate("Cisco AnyConnect - Banner")
time.sleep(0.2)

# Click Accept button
keyboard.send_key("<enter>")
time.sleep(0.1)
