import os
import  Core.configure as config
from Core.fetch_data import Fetch
'''
This is the main point of the app

This app scrap data from Linkedin :
- job-url or seach url
- urls.txt 


username : trw01212@toaik.com
passwrod : zzahmedzz1212
'''
if __name__ == '__main__':
    
    print('1.txt file \n2-search url or job\n')

    while True:
        choice = input("What is Ur Choice? : ")

        # check if the value is digit
        if choice.isdigit():
            # check if the value is 1 or 2 
            choice = int(choice)
            if choice == 1:

                print('txt file')
                # if the urls.txt dose not exists make one 
                # and tell the user to put the urls and re run the app
                if not os.path.exists(f"{os.getcwd()}/{config.URLS_TXT}"): 
                    file = open(config.URLS_TXT, 'w')
                    file.write('')
                    print('urls.txt is created put your urls in it and re turn the app')

                else: # here the app search for every line url
                    # get the urls from urls.txt

                    with open('urls.txt', 'r') as urls:
                        for url in urls:
                            print(Fetch.get_data(url.strip()))


                break
                
            elif choice == 2:
                print('search url or job')
                break

            else:
                print("This value dose't exist...\n")

        else:
            print("This value is not digit try again...\n")
    
