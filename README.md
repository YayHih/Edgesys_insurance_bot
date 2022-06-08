This program is a bot scraper, designed to scrape a database for relavant information on independent insurance companies in a certian state.

Instalation/dependencies:
As this is a python based program, the latest version of python is recomended as well as a IDE such as Microsoft Visual Studio.
Once both have been installed, one can install selenium through python's internal package installer, pip.
Then, one must install chrome driver (make sure that the chrome driver version that you install is works with the version of chrome that you have) and make sure to have it in its own folder that is easy to find.
Finaly you must create an exception in your enviorment varibles and add the folder where you put the chrome driver instalation as a path. 
This can be done by going to system properties clicking on Enviorment Varibles, then under System varibles, pressing on PATH, pressing edit and adding a new enviorment varible where you have just installed chrome driver. 

FILES:
Once this program has finished compiling it should create/ update 4 text files which each pertain to the program it has just ran.

File #1 is agents.txt; in this file, the company name, address, phone number, website and up to 5 socials are shown with a semi-colon seperating them for convience sake.

File #2 is a timing file, which shows how long it took for the program to compile in, as well as where it slowed down and such.

FIle #3 is an error info file; this file collects all of the places that it gets an error and prints them all into a file for your later convience.

File #4 is a log file, it collects the data of all runs and appends all of the data into one file.

TERMINAL:
Every time you start a new index the program will give you a list of companies it has completed and a list that it still has yet to go. It is also equiped with a reudamentry alogorithm to predict of quickly it will finish however, it is frequient that this algorithm is off by around 10 minutes. 

When it has succsefully completed one company it will print out a messege like this:

 Finished: 1 Number in list # 1 in Index: 0 Company Name: (John Doe Insurance Agency LLC) Time elapsed: 0:00:05.365904
 
However, sometimes when it does not find the company in question it will print out an error like this, and write down the failed company in its error log (shown above).

https://www.insurancecompanies/johndoeinsurnace.com
John Doe Insurance Services
 Finished: 75 error #1 error, company #47 number in index: 1 a: 1 x: 2 ################################################################################################################
 
Once the program has finished it should give out a messege similar to this:
Time spent: 0:10:19.705580
compiled in :
0:10:19.707068
errors found :
4/121
percentage not found :
3.306%
Number in Index: 12 highest num in list: 12

Modifications/Alterations:
The way that I am identifying what to scrape is based off of their CSS ID, as it was proven that this was the fastest way scrape with a selenum webdriver. 
Link here, https://www.linkedin.com/pulse/which-selenium-webdriver-locator-faster-zhimin-zhan-1c/
Shown below is the address selector of the code:
address_css_selector = '.card.shadow-sm.mb-4 .row.no-gutters.flex-column-reverse.flex-sm-row.text-center.text-sm-left .col.position-static .card-body .text-gray-700.text-sm'
This address can be found by going into developer mode and by clicking on an element with cntrl+shift+c and looking on the bottom right corner. One important thing to note is that while classes are indicated with a '.' before them, paragraphs and a's are denoted by p's and a's. 

Another thing to note is that one looking through an index, such as with this line:
anchor_tag = driver.find_elements(By.CSS_SELECTOR, item_css_selector)[i]
It is important to make sure that you specify driver.find_element"s" rather than driver.find_element, otherwise it will return some pretty nasty errors.
