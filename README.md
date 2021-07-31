# APARTMENTS 

Real estate aplication - Exam project, for educational purposes, within Python Web Framework module, SoftUni 

## Description

Apartments is a real estate web aplication. Users can find out about current offers available on the real estate market, can post their own or follow information about what is happening on the market in the industry. 

The application has a public part, a private part and an administrative part.

In the public part, users are unauthenticated but they can view all published ads and their details. They can filter and search for property according to different criteria. They can send inquiries for market valuations, sales and management of real estate. These actions are allowed without being authenticated or registered user.

To be in the private part of the site, users must be registered and logged in. After logging in, users have access to everything as in the public part, but also have their own profile to upload and store published ads. Registered and logged in user, can edit and delete their own ads and profile.

In the administrative part, the superuser has the rights of the first group, the rights of the second for his own profile. Additionally the superuser has access to admin, storred users inquiries. He can create market info ads. 


The project has four main modules. Each module is created and separated from the others, based on its functionality and can exist independently as such.

1. Apart-module - This module contains the models, forms and functionality of the main object in the project - apartment. An object is created and is associated with a key to the user who creates it. There is a search form In the listing template according to set criteria.

2. Accounts module - the module contains the user model and the logic for log in, log out and register. After the initial registration, the user has the opportunity to complete his account, to see a portfolio of ads uploaded by him, to edit or delete them.

3. Inquiry module - the module contains models, logic and forms for sending inquiries from users to the administrator. There is a temlate to list inquiries and a search form in it, available only to the administrator.

4. Market information module - models, forms and logic for creating publications by the administrator, accessible to all users.

5. Core- module Core is a module that contains validation template tags and other logic.


## Executing program

Django version 3.2.4 <br/>
PostgreSQL ORDBMS<br/>
https://github.com/RadkaValkova/Apartments

## Authors

Radka Valkova<br/>
Exam project, for educational purposes, within Python Web Framework module, SoftUni 



