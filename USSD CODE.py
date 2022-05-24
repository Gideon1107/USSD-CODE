#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:03:05 2022

@author: gideon
"""


def program():
    def main_page():
        print("""
        1. Data plans
        2. Social Bundles
        3. Balance check
        4. Borrow credit 
        5. Gift Data 
        6. Hot Deals""")
    

    def data_plans():
        print("""
        Buy Data plans 
        1. Daily 
        2. Weekly 
        3. Monthly 
        0.<< Back""")
        reply = input("Reply: ")
        if reply == "0":
            main_page()
        elif reply == "1":
            daily_data()
            reply = input("Reply: ")
            if reply == "0":
                data_plans()
        elif reply == "2":
            weekly_data()
            reply = input("Reply: ")
            if reply == "0":
                data_plans()
        elif reply == "3":
            monthly_data()
            reply = input("Reply: ")
            if reply == "0":
                data_plans()
                
    def daily_data():
        print("""
        Daily data page
        0.<<Back""")
        
    def weekly_data():
         print("""
        Weekly data page
        0.<<Back""")
    def monthly_data():
         print("""
        Monthly data page
        0.<<Back""")

    def social_bundles():
        
        print("""
        Social Bundles
        1. Whatsapp 
        2. Facebook 
        3. Instagram 
        0.<< Back""")
        reply = input("Reply: ")
        if reply == "0":
            main_page()
        elif reply == "1":
            whatsapp()
            reply = input("Reply: ")
            if reply == "0":
                social_bundles()
        elif reply == "2":
            facebook()
            reply = input("Reply: ")
            if reply == "0":
                social_bundles()
        elif reply == "3":
            instagram()
            reply = input("Reply: ")
            if reply == "0":
                social_bundles()
    def whatsapp():
        print("""
        Whatsapp data page
        0.<<Back""")
    def facebook():
        print("""
        Facebook data page
        0.<<Back""")
    def instagram():
        print("""
        Instagram data page
        0.<<Back""")

    def balance_check():
        
        print("""
        Your available is #498.54 
        0.<< Back""")
        reply = input("Reply: ")
        if reply == "0":
            main_page()

    def borrow_page():
        
        print("""
        You are not eligible to borrow 
        0.<< Back""")
        reply = input("Reply: ")
        if reply == "0":
            main_page()

    def gift_data():
        print("""
        Gift data page 
        0.<< Back""")
        reply = input("Reply: ")
        if reply == "0":
           main_page()

    def hot_deals():
        
        print("""
        Hot deals page 
        0.<< Back""")
        reply = input("Reply: ")
        if reply == "0":
            main_page()
    

    print('Welcome to MTN online \n \x1B[3mLOADING\x1B[0m.....')
    
    USSD = input("Enter USSD code: \n")
    if USSD == "*131#":
        main_page()
    else: 
        print('USSD ERROR')
    while True:
        RESPONSE = input("Reply: ")
        if RESPONSE == "1":
            data_plans()
        elif RESPONSE == "2":
            social_bundles()
        elif RESPONSE == "3":
            balance_check()  
        elif RESPONSE == "4":
            borrow_page()
        elif RESPONSE == "5":
            gift_data()
        elif RESPONSE == "6":
            hot_deals()
        else:
            print('incorrect option, try again')
            continue
program()        
        
        
        
        
        
        
        
        
        
        
        
        