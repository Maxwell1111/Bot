from open_webdriver import open_webdriver

#define time
import time

def main():

    with open_webdriver(headless=False) as driver:

        # All Chromium / web driver dependencies are now installed.

        driver.get("https://pubmed.ncbi.nlm.nih.gov/")

        assert driver.title == "PubMed"
        #find search bar
        search_bar = driver.find_element_by_name("term")
        #type in search bar
        search_bar = driver.find_element_by_name("term")
        search_bar.send_keys("chk-1")








        
        search_bar.submit()

        #for each article in the document
        for article in driver.find_elements_by_class_name("full-docsum"):
            #print the title
            text=article.text
            print(article.text)

            
            
        #make list of all the links
        links = driver.find_elements_by_xpath("//a[@href]")
        #limit to 10 links
        links = links[:10]

        #print all the links in headings
        for link in links:
            print(link.text)
        #print all the links
        for link in links:
            print(link.get_attribute("href"))
        #print all the links in headings
        #for link in links:

        
            

       
        #find abstract
        abstract = driver.find_element_by_class_name("abstract-content")
        print(abstract.text)
        #search content for keywords
        if "fromulation" in abstract.text:
            print("fromulation is in the abstract")
        else:
            print("fromulation is not in the abstract")
        
        is_done = False
        while not is_done:
            #find next button
            next_button = driver.find_element_by_class_name("next")
            #click on next button
            next_button.click()
            #find abstract
            abstract = driver.find_element_by_class_name("abstract-content")
            print(abstract.text)
            #search content for keywords
            if "fromulation" in abstract.text:
                print("fromulation is in the abstract")
                is_done = True
            else:
                print("fromulation is not in the abstract")
            

        
        
        


       
          

        #leave page open for 5 seconds
        time.sleep(5)


        
                
        



if __name__ == "__main__":
    main()