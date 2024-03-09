## DEPENDENCIES
1. Install selenium: pip install selenium

## CONFIGURATION (config.json)

>> chromeUserProfilePath:
    1. Find user data profile folder for chrome, usually in "C:\\Users\\[YOUR-USERNAME]\\AppData\\Local\\Google\\Chrome\\User Data"
    2. Replace chromeUserProfilePath key in json with your user profile chromeUserProfilePath.

>> azureNetworkingTabURL:
    1. The url to the network tab of the azure openai service

>> listOfIps:
    1. The IPs that can access this service

## RUN (network_switcher.py)
    1. Close all existing Chrome windows and tabs
    2. Run "python network_switcher.py"
    3. Login to your Azure Account
    4. Press Enter in the terminal window
    5. The script will do the rest: 
        -- If "All Networks" is selected, it will switch to "Selected Networks" and all IP addresses from config.json will be added.
        -- If "Selected Networks" is selected, it will switch to "All Networks"