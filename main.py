import os
import  Core.configure as config
from Core.fetch_data import Fetch
'''
This is the main point of the app

This app scrap data from Linkedin :
- urls.txt 
- single link

'''
if __name__ == '__main__':
    
    print('1.txt file \n2-single link\n')

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
                    urls_list = []

                    # get all urls and append them to urls_list
                    with open('urls.txt', 'r') as urls:
                        for url in urls:
                            urls_list.append(url.strip())
                            
                    Fetch.get_data(urls_list, 1)

                break
                
            elif choice == 2:
                # single link
                url = input('Enter the url start with https:// : ')
                Fetch.get_data(url)
                break

            else:
                print("This value dose't exist...\n")

        else:
            print("This value is not digit try again...\n")
    
