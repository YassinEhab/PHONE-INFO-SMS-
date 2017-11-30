#!/usr/bin/env python3
#CODER:MRZ(YASSIN EHAB)
#PHONE(INFO,SMS)
#EGYPT:>

#lets start bb
# -*- coding: utf-8 -*-
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
face=("https://www.facebook.com/login/")
twitter=("https://twitter.com/account/begin_password_reset?account_identifier=")
google=("https://accounts.google.com/signin/v2/identifier?")
MRZ="""
    ███╗   ███╗██████╗ ███████╗
    ████╗ ████║██╔══██╗╚══███╔╝
    ██╔████╔██║██████╔╝  ███╔╝ 
    ██║╚██╔╝██║██╔══██╗ ███╔╝  
    ██║ ╚═╝ ██║██║  ██║███████╗
    ╚═╝#MRZ ╚═╝╚═╝  ╚═╝╚══════╝
    #SPOOKS,PHONE(INFO,SMS)
    """
def home():
    print(MRZ)
    print("            PHONE(INFO,SMS)")
    print("1)SMS SITES")
    print("2)PHONE INFO")
    what=input("SELECT A NUMBER: ")
    what=int(what)
    if what==1:
        os.system('cls'); SMS()
    elif what==2:
        os.system('cls'); INFO()
def SMS():
    print(MRZ)
    print("")
    print("[1]  http://www.sendsmsnow.com/")
    print("[2]  http://www.txt2day.com/")
    print("[3]  http://www.24sms.net/")
    print("[4]  http://www.txtdrop.com/")
    print("[5]  https://www.opentextingonline.com/")
    print("[6]  https://textforfree.net/")
    print("[7]  http://www.sendanonymoussms.com/")
    print("[8]  https://txtemnow.com/")
    print("[9]  https://www.smsgenie.co/")
    print("[10] http://www.afreesms.com/freesms/")
    sleep(3)
    print("")
    print("AFTER 5 SECONDS YOU WILL RETURN TO MENU...")
    sleep(5)
    os.system('cls'); home()
def INFO():
    print(MRZ)
    number=input("ENTER PHONE NUMBER: ")
    if len(number)==11:
        if ("010") or ("011") or ("012") or ("015") in number:
            print("VALID NUMBER...")
            print("Country:	   EG(Egypt)")
            print("Phone type: mobile")
            print("Timezones:  Africa")
            if ("011") in number:
                print("Carrier: Etisalat")
            elif ("010") in number:
                print("Carrier: Vodafone")
            elif ("012") in number:
                print("Carrier: Orange(Mobilnil)")
            elif ("015") in number:
                print("Carrier: Telecom Egypt")
            #=======================================================#
            driver = webdriver.PhantomJS(executable_path=r'phantomjs.exe', port=0)
            #=======================================================#
            driver.get(face)
            driver.find_element_by_xpath(".//*[@id='email']").send_keys(number)
            driver.find_element_by_xpath(".//*[@id='pass']").send_keys(number)
            driver.find_element_by_xpath(".//*[@id='loginbutton']").click()
            sleep(1)
            facetest=driver.find_element_by_xpath(".//*[@id='globalContainer']/div[3]/div/div/div").text
            facetest1=("The password that you've entered is incorrect. Forgotten password?")
            if facetest==facetest1:
                 print("Facebook:FOUND")
            else:
                print("Facebook:NOT FOUND")
            #===========================================================#
            driver.get(twitter+number)
            driver.find_element_by_xpath("//input[@value='Search']").click()
            sleep(1)
            twittertest=driver.find_element_by_xpath("html/body/div[2]/div/div[1]").text
            twittertest1=("We couldn't find your account with that information")
            if twittertest==twittertest1:
                print("Twitter:NOT FOUND")
            else:
                print("Twitter:FOUND")
            #===========================================================#
            driver.get(google)
            driver.find_element_by_xpath(".//*[@id='identifierId']").send_keys(number)
            driver.find_element_by_xpath(".//*[@id='identifierNext']/content/span").click()
            googletest=driver.find_element_by_xpath(".//*[@id='headingText']").text
            sleep(3)
            googletest=driver.find_element_by_xpath(".//*[@id='headingText']").text
            googletest1=("Welcome")
            if googletest==googletest1:
                print("Google:FOUND")
                print("Google+:FOUND")
                print("Youtube:FOUND")
                print("Gmail:FOUND")
            else:
                print("Google:NOT FOUND")
                print("Google+:NOT FOUND")
                print("Youtube:NOT FOUND")
                print("Gmail:NOT FOUND")
            #===========================================================#
            sleep(3)
            print("")
            print("AFTER 5 SECONDS YOU WILL RETURN TO MENU...")
            sleep(5)
            os.system('cls'); home()
        else:
            print("INVALID NUMBER OR NOT EGYPTION NUMBER!")
            sleep(3)
            print("")
            print("AFTER 5 SECONDS YOU WILL RETURN TO MENU...")
            sleep(5)
            os.system('cls'); home()
    else:
        print("INVALID NUMBER OR NOT EGYPTION NUMBER!")
        sleep(3)
        print("")
        print("AFTER 5 SECONDS YOU WILL RETURN TO MENU...")
        sleep(5)
        os.system('cls'); home()
home()
    
