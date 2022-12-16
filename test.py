from open_webdriver import open_webdriver

def main():

    with open_webdriver(headless=False) as driver:

        # All Chromium / web driver dependencies are now installed.

        driver.get("https://www.google.com")

        assert driver.title == "Google"



if __name__ == "__main__":
    main()