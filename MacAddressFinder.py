"""
This script finds the mac address of a device on the same network as you.
"""
from getmac import get_mac_address, getmac

while True:
    # Constants
    ip_mac = get_mac_address(ip = 'x.x.x.x')

    # We ask the user for the IP of the device
    device_ip = input('[*] Enter the IP of the device: ')
    mac_addy = str(getmac.get_mac_address(ip = device_ip))
    if mac_addy != 'ff:ff:ff:ff:ff:ff':
        # If the device can be found, then we print out the mac address
        print('[*] Mac address of '+ str(device_ip) + ' is: ' + (mac_addy))
    elif mac_addy == 'ff:ff:ff:ff:ff:ff':
        # If the device cannot be found, then we print out that the device cannot be found
        print('[*] Device cannot be found!')

    # If they have another device that they would like to find the mac address of
    ask_go_again = input('[*] Would you like to find another mac address?: ')
    if ask_go_again == 'Yes' or ask_go_again == 'yes':
        # If yes, then loop back to the beginning
        continue
    elif ask_go_again == 'No' or ask_go_again == 'no':
        # If no, then we end code execution
        break
    else:
        # If they do not answer , then quit anyways
        print('[*] I will quit anyways!')
        break
