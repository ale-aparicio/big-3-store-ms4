# The Big 3 Store

[View live website](https://big-3-store.herokuapp.com)

The Big 3 Store is a website dedicated to the selling of products related to the 3 best selling shonen manga's of the 2000's. It is designed to be easily accesible from a range of devices, making it easy to navigate and browse through the different available products. 

![Display of the Website]()

## Contents ##

- [Mission Statement](#mission-statement)
- [Target Audience](#target-audience)
- [Business Objectives](#business-objectives)
- [User Experience](#user-experience)
- [UX](#ux)
    - [Project Strategy](#project-strategy)
    - [Project Scope](#project-scope)
        - [User Demographics](#user-demographics)
        - [User Requirements](#user-requirements)
        - [Functional Requirements](#functional-requirements)
        - [User Stories](#user-stories)
        - [Constraints](#constraints)
        - [Business Rules](#business-rules)
        - [Key Features](#key-features)
    - [Site Map](#site-map)
    - [Wireframes](#wireframes)
    - [Design Choices](#design-choices)
        - [Fonts](#fonts)
        - [Colours](#colours)
- [Technologies](#technologies)
    - [Integrated Development Environment](#integrated-development-environment)
    - [Languages](#languages)
    - [Database](#database)
    - [Storage](#storage)
    - [Payments](#payments)
    - [Frameworks](#frameworks)
    - [Libraries and Tools](#libraries-and-tools)
    - [Browser Support](#browser-support)
- [Structure](#structure)
    - [Information Architecture](#information-architecture)
        - [Products Models](#products-models)
        - [Checkout Models](#checkout-models)
        - [Profiles Models](#profiles-models)
        - [Basket Models](#basket-models)
    - [Features Implemented](#features-implemented)
        - [Features Implemented in Phase 1](#features-implemented-in-phase-1)
            - [Features Included In Base Template](#features-included-in-base-template)
            - [Contact](#contact)
            - [User Authentication System](#user-authentication-system)
            - [Products](#products)
            - [Messaging System](#messaging-system)
            - [Basket](#basket)
            - [Checkout](#checkout)
            - [User Profile](#user-profile)
        - [Features To Be Implemented In Future Development Phases](#features-to-be-implemented-in-future-development-phases)
        - [Design Changes During The Phase 1 Development](#design-changes-during-the-phase-1-development)
    - [Responsive Styling](#responsive-styling)
    - [Python Code Logic](#python-code-logic)
    - [Form Validation](#form-validation)
    - [JavaScript Code Logic](#javascript-code-logic)

- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Mission Statement ##

To provide the best quality product at the most affordable price possible.

## Target Audience ##

The target audience for **The Big 3** is fans of the popular Anime's featured on our store. We attempt to provide the highest possible quality at affordable prices so that the products offered can be accesible to everyone.

## Business Objectives ##

Although the business is merely for educational purposes it's overall design and development strategies have been taken from a realistic perspective: 

- To Provide an easy to navigate, well designed online shop that offers secure purchases, and a variety of products that tries to meet the users demands.

- Provide the ability for users to review and leave feedback on products for future customers to feel confident in the product they might be interested in.

- Grow the shop over time, offering more variety and quantity of the types of products we offer to meet even the niche's of demands.

## User Objectives ##

- Purchase medium to high quality products from the 3 anime's featured in the website
such as apparel, figures, and props. 

- See other user's reviews and feedback to give new users the necesarry information to encourage them to purchase said item.

- Contact the business about an order or to provide feedback about the website or more product they would like to see featured in the shop.

- Make an account to be able to see their order history and edit and save their personal information for future purchases.

# User Experience
## Project Strategy 
The strategies used to build the website and the business as a whole are listed below: 

### The Products

#### Apparel:
The apparel offered in the website are currently from a variety of providers, and quality controlled by us to ensure both the quality and the pricing of the product has been justified to maximize customer satisfaction.

#### Figures:
The figures have been carefully selected and carefully priced based on the materials and amount of detail the figure has aswell as the availablity of each figure.

#### Props:
The Props available are clear replicas of some of the memorable wear and accesories of the characters showcased in the shows. We attempt to offer the most identical products to the items displayed in the show.

### Customer Reviews 
Customer Reviews are important for the overall ecosystem of the business as it provides happy and disatisfied customers a way to express their views on products they have purchased and by doing so giving new customers and us as business owners feedback on popular products aswell as lacking products that might need to me replaced, improved or removed. 

## Project Scope
### User Demographics 
- The primare users of the site will be fans of the featured shows looking for merchandise or memorabilia from shows they watched as kids or have just started watching it's targeted for all ages. 

- The website is simple, easy to use and easy to navigate that displays the necessary information for the user to be able to find what they're looking for with ease. 

### User Requirements
- Simple and well laid out
- Easy to navigate
- Clean with the necessary information
- Easy to make purchases
- Responsive design is required as users may be viewing the store from a mobile, tablet or desktop.
- The store should be secure since the use of a credit card is necessary to make a purchase as well as the users personal information to make a delivery.

### User Stories

As a **New Customer** I would like to be able to: 

- Understand the purpose of the website.
- View and navigate the site on all devices.
- Be able to explore the available products.
- Add products that are to my liking to my cart, so I can purchase them. 
- Be able to view the requirements for a free delivery to make my purchases according to those requirements.
- Recieve a confirmation my purchase has been made via email.
- Register to the site and be able to have my past orders displayed and my personal information saved for future purchases. 
- Contact the business with questions about past and current orders and with suggestions and feedback about possible future changes and current complaints.

As a **Registered User**, I would like to be able to:

- Sign in to my account.
- Sign out of my account. 
- Be able to recover a forgotten password.
- View and update my personal information.
- See my past orders.s.
- Edit previous Reviews.

As a **Business Owner**, I would liek to be able to: 

- Add, Edit and Delete Products. 
- Edit product prices
- Delete user reviews, in case they're of malicious intent
- Check customer 