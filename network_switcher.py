import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Read configuration for Chrome Driver executable path
with open("config.json", "r") as f:
    config = json.load(f)
chrome_user_profile_path = config.get("chromeUserProfilePath")

# Configure Selenium to connect to the existing Chrome instance
options = Options()
options.add_argument("--remote-debugging-port=9222")
options.add_argument(f'user-data-dir={chrome_user_profile_path}')

# Initialize WebDriver with the path to chromedriver if not in PATH
driver = webdriver.Chrome(options=options)

# Now you can control the existing Chrome window
driver.get('https://portal.azure.com')
input("Please login and press enter")

try:
    driver.get(config['azureNetworkingTabURL'])
    print("Loading Networks Tab")
    time.sleep(5)
    all_networks_checkbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[1]/main/div[3]/div[2]/section/div[1]/div[2]/div[2]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[5]/div[2]/div/div/ul/li[1]')
    selected_networks_checkbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[1]/main/div[3]/div[2]/section/div[1]/div[2]/div[2]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[5]/div[2]/div/div/ul/li[2]')
    save_networks_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[1]/main/div[3]/div[2]/section/div[1]/div[2]/div[2]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]')

    if all_networks_checkbox.get_attribute("aria-checked") == "true":
        print("All networks selected.")
        print("Switching to Selected networks.")
        selected_networks_checkbox.click()
        time.sleep(2)
        print("Adding IP addresses")
        for ip_index, ip_address in enumerate(config["listOfIps"]):
            ip_input = driver.find_element(By.XPATH, f'/html/body/div[1]/div[4]/div[1]/div[1]/main/div[3]/div[2]/section/div[1]/div[2]/div[2]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[7]/div[10]/div/div/div[2]/div/div[2]/div[1]/div[{ip_index+1}]/div[1]/div[1]/div/div[2]/div/div/div/input')
            ip_input.send_keys(ip_address)

        print("Added IP Addresses")
        time.sleep(2)
        print("Saving Network configuration")
        save_networks_btn.click()
        time.sleep(15)

    elif selected_networks_checkbox.get_attribute("aria-checked") == "true":
        print("Selected networks selected.")
        print("Switching to All networks.")
        all_networks_checkbox.click()
        print("Switched to All Networks")
        time.sleep(2)
        print("Saving Network configuration")
        save_networks_btn.click()
        time.sleep(15)

    else:
        print("None of all networks or selected networks was selected.")

    print("Closing driver..")
    driver.quit()

except Exception as e:
    print(f"Error, pls follow proper steps: {e}")


# if //*[@id="_weave_e_582"] aria-checked="true", all networks selected, send click to //*[@id="_weave_e_585"]
# iterate through ip addresses, go to
# /html/body/div[1]/div[4]/div[1]/div[1]/main/div[3]/div[2]/section/div[1]/div[2]/div[2]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[7]/div[10]/div/div/div[2]/div/div[2]/div[1]/div{index}/div[1]/div[1]/div/div[2]/div/div/div/input

# if //*[@id="_weave_e_585"] aria-checked="true", selected networks selected, send click to //*[@id="_weave_e_582"] and do nothing and print done
# after all done, click //*[@id="_weave_e_560"]
