# Tutanota-XCloud

A Python program to create Tutanota email accounts using Selenium and NordVPN.

### Language: 

- Python

### Flow diagrams:

### Requirements:

- NordVPN

### Libraries:

- ipapi==1.0.4
- names==0.3.0
- nordvpn_switcher==0.3.0
- PyAutoGUI==0.9.53
- PyGetWindow==0.0.9
- requests==2.28.1
- selenium==4.7.2
- webdriver_manager==3.8.5

### API:

- None

### Functions:

1. check_ip()
2. create_account()
3. generate_credentials()
4. generate_username()
5. main()
6. initialize_VPN()
7. rotate_VPN()
8. terminate_VPN()

### Procedures:

1.  Initialize NordVPN with the function `initialize_VPN`.
2.  Get the current location using the `requests` library.
3.  Set up the webdriver with the `webdriver` library.
4.  Loop through the months and generate credentials with the `generate_credentials` function.
5.  Rotate the VPN with the `rotate_VPN` function.
6.  Check the IP address with the `check_ip` function.
7.  Create the account with the `create_account` function.
8.  Terminate the VPN with the `terminate_VPN` function.
9.  Wait 5 minutes and increment the loop index.

### Resources:

1. GitHub

[https://github.com/kboghe/NordVPN-switcher](https://github.com/kboghe/NordVPN-switcher)


### Additional notes:

None

 
