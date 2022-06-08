# Writen by Martin Oka last update 5/31/2022
# link for chrome driver https://chromedriver.chromium.org/getting-started
# Dependancies: Python, Selenium (can be installed through pip)
# Make sure to set up two text documents agents.txt and test.txt to see full list of agencies
# make sure you set a add a path enviorment varible
# Plans for the future, multithread to make process more efficent
#https://analyticsindiamag.com/how-to-run-python-code-concurrently-using-multithreading/

PATH = "C:\webdrivers\chromedriver.exe"
from pickle import FALSE, TRUE
from unicodedata import name
from xmlrpc.client import Boolean
from numpy import number
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
startTime = datetime.now()

#^for timer that goes off at the reset of the first for loop
def main():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('window-size=800,600')
    driver_options.add_argument('start-maximized')
    driver_options.add_argument('headless')
    driver_options.add_argument('log-level=2')
    driver = webdriver.Chrome(options=driver_options)
    driver.get('https://www.trustedchoice.com/agent/wv/')
    #driver.get moves it to a certian website
    places_selector = '.row.mb-4'
    Number_in_index=0
    #defines what index it is on at the time
    total_comapnies = 0
    a=0
    i=0
    #most insurnace companies in a certian location (highest index num)
    counter=0
    full_counter=0
    error_counter=0
    #number of links in the website that are meant to be clicked on -1, in the same parent direcotry
    global number_of_links
    number_of_links = 1000
    link_counter=0
    #0015277 30 min

    avg_timing=5
    #data collection varibles
    all_information = ''
    timing_information = ''
    error_information = ''
    global highest_num_in_list
    highest_num_in_list=1
    first= TRUE
    item_css_selector = ".container-fluid.px-4 .agency-directory-body .font-condensed strong span"
    try:
        WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, item_css_selector)))
        total_comapnies = driver.find_element(By.CSS_SELECTOR, item_css_selector)
        
    except IndexError:
        print("unable to find companies")
        pass
    except:
        print("unable to find companies")
        pass
    
    print("Total independent companies: "+total_comapnies.text)
    total_comapnies = int(total_comapnies.text)
 

    while a < highest_num_in_list:
    #each time that it repeats it looks at the u(number it is on) to copy that information down
        while i <number_of_links:
        #moves on after it has gone through number of links+1            
            fail=False
            name_fail=False
            #resents the fail varible that moves on and displays an error
            item_css_selector = places_selector + ' .col-md-2.col-4  a'
            try:
                WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, item_css_selector)))
                #There are alot of ways to select the element but using CSS_SELECTOR was found to be the fastest, see here:https://www.linkedin.com/pulse/which-selenium-webdriver-locator-faster-zhimin-zhan-1c/
                num_agents = driver.find_elements(By.CSS_SELECTOR, item_css_selector)[i]
            except IndexError:
                    fail=TRUE
                    pass
            except:
                
                fail=TRUE
                pass
            if first:
                number_of_links= len(driver.find_elements(By.CSS_SELECTOR, item_css_selector))
                print("Number of locations:  "+str(number_of_links))
                print("Companies to go: "+str(total_comapnies-full_counter)+ " Total estamated time remaining: "+ str(round(((.04*number_of_links*(highest_num_in_list-1)-total_comapnies*.04)+(avg_timing*(total_comapnies)))/60, 2) )+" Min")
                first=False
            #---------------------------------------------Finds how many companies there are in a certian link by what the website says
            if not fail:
                if not num_agents.text[-3]=='(':
                    x=10*int(num_agents.text[-3])+int(num_agents.text[-2])
                else:
                    x=int(num_agents.text[-2])
                #if the amount of times that it has gone around is higher than the amount of companies in the list, it will just move on. 
                if highest_num_in_list < x:
                    highest_num_in_list=x
                if Number_in_index >= x:
                    i+=1
                    pass
                else:
                    #--------------------------------------------------------LINK Selector
                    item_css_selector = places_selector + ' .col-md-2.col-4  a'
                    try:
                        WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, item_css_selector)))
                    except IndexError:
                        fail=TRUE
                        pass
                    except:
                        print('Error clicking link on')
                        return
                    anchor_tag = driver.find_elements(By.CSS_SELECTOR, item_css_selector)[i]
                    driver.get(anchor_tag.get_attribute('href'))
                    
                    #--------------------------------------------------- ADDRESS Selector
                    address_css_selector = '.card.shadow-sm.mb-4 .row.no-gutters.flex-column-reverse.flex-sm-row.text-center.text-sm-left .col.position-static .card-body .text-gray-700.text-sm'
                    try:
                        WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, address_css_selector)))
                        address_element = driver.find_elements(By.CSS_SELECTOR, address_css_selector)[Number_in_index]
                        #                                                                               ^ Specifies which company it will pick
                    except IndexError:
                        fail=TRUE
                        pass
                    except:
                        fail=TRUE
                        name_fail=TRUE
                        pass
                    #----------------------------------------------------------------------------------NAME of Agency Selector
                    address_css_selector = '.card.shadow-sm.mb-4 .row.no-gutters.flex-column-reverse.flex-sm-row.text-center.text-sm-left .card-title.btn.btn-link.font-weight-bold.text-gray-700.text-xl.text-sm-left.p-0.mb-1.stretched-link.rounded-0'
                    try:
                        WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, address_css_selector)))
                        place_name_element = driver.find_elements(By.CSS_SELECTOR, address_css_selector)[Number_in_index]
                    except IndexError:
                        fail=TRUE
                        name_fail=TRUE
                        pass
                    except:
                        fail=TRUE
                        name_fail=TRUE
                        pass
                    #------------------------------------------------------------------------------- Phone Number Selector
                    address_css_selector = '.card.shadow-sm.mb-4 .row.no-gutters.flex-column-reverse.flex-sm-row.text-center.text-sm-left .col.position-static .card-body .text-sm .stretched-link-override'
                    try:
                        WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, address_css_selector)))
                        phone_name_element = driver.find_elements(By.CSS_SELECTOR, address_css_selector)[Number_in_index]
                    except IndexError:
                        fail=TRUE
                        pass
                    except:
                        fail=TRUE
                        pass
                    if not fail:
                        counter+=1
                        full_counter+=1
                        link_counter+=1
                        i+=1
                        timing_information += str(datetime.now() - startTime) +"\n"
                        print(" Finished: " + str(counter)+' Number in list # ' + str(i), 'in Index: ' +str(Number_in_index)+" Company Name: (" +place_name_element.text + ') Time elapsed: '+str(datetime.now() - startTime))
                        all_information += place_name_element.text + ";" + address_element.text + ";"+ phone_name_element.text 
                        #if it has found information about the company then it will procide to try and find their website
                        
                        item_css_selector = '.card.shadow-sm.mb-4 .row.no-gutters.flex-column-reverse.flex-sm-row.text-center.text-sm-left .col.position-static .card-body .mt-2 .agency-directory-profile-button.btn.btn-sm.btn-outline-secondary.stretched-link-override'
                        try:
                            WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, item_css_selector)))
                            link2 = driver.find_elements(By.CSS_SELECTOR, item_css_selector)[Number_in_index]
                        except IndexError:
                            fail=TRUE
                            pass
                        except:
                            fail=TRUE
                            pass
                        if not fail:
                            driver.get(link2.get_attribute('href'))
                            
                                #--------------------------------------------------- link 2 - clicks on the first web link bringing us to the webpage
                            item_css_selector = ".col-lg-8 .mb-2.mb-md-1.font-condensed a"
                            try:
                                WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, item_css_selector)))
                                link3 = driver.find_element(By.CSS_SELECTOR, item_css_selector)
                            except IndexError:
                                fail=TRUE
                                pass
                            except:
                                fail=TRUE
                                pass
                            if not fail:
                                all_information +=  ";"+link3.get_attribute('href')
                                #Link 3 just graps their website
                                o=0
                                while o <=5:
                                #repeats five times, or until no more social links
                                    item_css_selector = ".col-lg-8 .mb-2.mb-md-1 .text-decoration-none"
                                    try:
                                        WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, item_css_selector)))
                                        link4 = driver.find_elements(By.CSS_SELECTOR, item_css_selector)[o]
                                        #grabs the link
                                    except IndexError:
                                        fail=TRUE
                                        pass
                                    except:
                                        fail=TRUE
                                        pass
                                    if not fail:
                                        all_information +=  ";"+link4.get_attribute('href')
                                    else:
                                        pass
                                    o+=1
                                    
                                all_information += '\n'
                                driver.back()
                                driver.back()
                                #adds a return then returns back to home once all information found
                            else:
                                #for clairty sake, puts in no thing found then returns back to home
                                all_information +=  ";"+"no website found"+";"+"no social profiles"+ '\n'
                                driver.back()
                                driver.back()
                                pass
                        else:
                            all_information += '\n'
                            driver.back()
                    else:
                        full_counter+=1
                        print(driver.current_url)
                        if not name_fail:
                            print(place_name_element.text)
                            error_information+=place_name_element.text+";"+driver.current_url+"; Number in index"+ str(Number_in_index)+"\n"
                        else:
                            print("cannot find name")
                            error_information+=driver.current_url+"; Number in index"+ str(Number_in_index)+"\n"
                        error_counter+=1
                        link_counter+=1
                        i+=1
                        print(" Finished: "+ str(counter)+" error #"+str(error_counter)+ ' error, company #'+str(i)+" number in index: "+str(Number_in_index)+" a: "+str(a)+" x: "+str(x)+" ################################################################################################################")
                        #Prints an error to show that the comapny does not have the nessary information to copy down.    ^(how many times around) ^(in company number)
                        # While it could go ahead and continue, most of these insurance companies that do not have their viatal information on the home page, are mostly ghost companies or backrupt.
                    
                        driver.back()
        else:
            
            i=0
            Number_in_index+=1
            a+=1
            print("Inedexs to go: "+str(highest_num_in_list-Number_in_index)+" Index number: "+str(Number_in_index)+" ----------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Companies to go: "+str(total_comapnies-full_counter)+ " Total estamated time remaining: "+ str(round(((.04*number_of_links*(highest_num_in_list-Number_in_index)-total_comapnies*.04)+(avg_timing*(total_comapnies-full_counter)))/60, 2) )+" Min")
            print("Time spent: "+str(datetime.now() - startTime))
       
        
        
        
        


    with open('agents.txt', 'w') as f:
        f.write(all_information)
        # print('finished')
        # print(all_information)
        print("compiled in :")
        print((datetime.now() - startTime))
        print("errors found :")
        print(str(error_counter)+"/"+str(total_comapnies))
        print("percentage not found :")
        err_percentage = (error_counter/total_comapnies)*100
        print(str(round(err_percentage, 3))+"%")
        file2 = open("timing.txt", "w")  # write mode
        file2.write(timing_information)
        #shows the statisitcs of how quickly it took to compile
        file2.close()
        file3 = open("error_info.txt", "w")  # write mode
        file3.write(error_information)
        #shows the statisitcs of how quickly it took to compile
        file3.close()
        file3 = open("log.txt", "a")  # write modeprint()
        file3.write(driver.current_url+" "+str(round(err_percentage, 3))+"%"+"  ammount incorrect: "+str(error_counter)+"/"+str(total_comapnies)+" compiled in: " +str(datetime.now() - startTime)+" Perdicted compelation time: "+str(round(((.04*number_of_links*(highest_num_in_list-1)-total_comapnies*.04)+(avg_timing*(total_comapnies)))/60, 2) )+"\n")
        #shows the statisitcs of how quickly it took to compile
        file3.close()
        print("Number in Index: "+ str(a)+" highest num in list: "+str(highest_num_in_list))
    

if __name__ == '__main__':
    main()