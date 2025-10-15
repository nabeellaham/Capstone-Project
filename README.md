CarFinde Website
A simple web app to browse and list cars for sale. Users can view cars, create accounts, and manage their own car listings.

      Main Features

1. For All Visitors
    Browse all available cars without login

    View car details and photos
 
    Search and filter by brand, model, price

2. For Registered Users
    Create account and login

   Add new car listings

   Edit or delete their own cars

   Personal page for their listings

3. For Admin
    Full control via admin panel

    Manage all cars and users

4. Built With
    Django - Main framework
     
    python3 

    HTML & CSS - User interface

    SQLite - Database (for development)
    

       
      Basic User Stories

         1.As a Site Visitor

I can see car photos, prices, and basic details on the main page

I can use search to find cars by brand or model

I can filter cars by price and type

I can view detailed information when I click on a car
         
        2.As a Registered User
I can create an account with email and password

I can log in to my account securely

I can add my own car listings with photos and details

I can edit my car listings if I make a mistake or need to update

I can delete my car listings when they sell

I can mark my cars as "sold" when they're no longer available

I can see all my listings in one place

        3.Advanced Features
For Better Searching
I can filter by car year, Model, and Brand

I can sort cars py price

        4.As an Administrator
I can manage all user accounts

I can remove inappropriate listings

I can verify car information

I can help users with problems

I can see website statistics and activity


erd for the car finder

<img width="733" height="420" alt="erd_car_finder" src="https://github.com/user-attachments/assets/9bbcca47-a5ba-44c9-9cd6-42ff6d258daf" />




Quick Installation
     1.Prerequisites

Python 3.8 or higher

pip package manager
 
git or Windows PowerShell


 
         Step 1: Clone the Repository
 
#open git bash py Left mouse click and click on open git bash here
run this     ==> git clone https://github.com/nabeellaham/Capstone-Project.git
and run this ==> cd Capstone-Project
 
         Step 2: run this commands 1 py 1
 
 1.==> pipenv shell
 2.==> pipenv install
 3.==> python manage.py makemigrations
 4.==> python manage.py migrate
 5.==> pipenv install django
 6.==> pipenv install psycopg2-binary
 7.==> python manage.py runserver

         step 3 : open the website 
         open http://127.0.0.1:8000/
