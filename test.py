import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from optparse import OptionParser


def parse_arguments():
    parser = OptionParser()
    parser.add_option("--user_name", action="store", dest="user_name",
                      help="BravoSystems Artifactory instance URL", default=None)
    parser.add_option("--user_password", action="store", dest="user_password",
                      help="List of networks to revert", default=None)
    
    options, _ = parser.parse_args()
    return options

def test_method():

    arguments = parse_arguments()

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    driver.get('https://trello.com/login')

    print('Start ...')

    # enter user name in trello
    user_name = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'user')))
    print('User Name: {}'.format(arguments.user_name))
    user_name.send_keys(arguments.user_name)

    # click continue on trello page
    trello_continue_user_name_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'login')))
    trello_continue_user_name_button.click()

    # click continue
    continue_user_name_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'login-submit')))
    continue_user_name_button.click()

    # enter user password
    user_pass = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'password')))
    print('User Password: {}'.format(arguments.user_password))
    user_pass.send_keys(arguments.user_password)

    # click login button
    click_login = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'login-submit')))
    click_login.click()

    # click login button
    gettext = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'boards-page-board-section-header-name')))
    
    print('Text to print : {}'.format(gettext.text))


    print('Stop ...')



if __name__ == "__main__":
    test_method()