import time

# ==============================================================================

STARTUP_TIME = 0.5         # Needs to be enough for the existing window to focus
DISCONNECT_TIME = 1.5      # Needs to be enough for the client to disconnect

# ==============================================================================

# Wait for AutoKey to start
time.sleep(STARTUP_TIME)

window.activate("Cisco AnyConnect Secure Mobility Client")
time.sleep(0.2)

# Expects to be focused on the Details... button in the Statistics tab

# Focus on the Statistics tab header
keyboard.send_key("<tab>")
time.sleep(0.1)

# Switch to Connection tab
keyboard.send_key("<left>")
time.sleep(0.1)

# Navigate to Disconnect button
keyboard.send_key("<tab>") # Config button
time.sleep(0.1)
keyboard.send_key("<tab>") # Disconnect button
time.sleep(0.1)

# Click the Disconnect button
keyboard.send_key("<enter>")

# Wait for disconnection
time.sleep(DISCONNECT_TIME)

# Close window gracefully
window.close("Cisco AnyConnect Secure Mobility Client")
