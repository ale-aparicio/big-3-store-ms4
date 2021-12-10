# Testing 

![Display of the Website](media/README/big-3-mockup.jpg)

[View live website](https://big-3-store.herokuapp.com)

[Return to the README file](README.md)
## Automated Testing 
### HTML

All **HTML** code has been validated using [W3C Validator](https://validator.w3.org/) and came out with no errors.

### CSS 

All **CSS** code files have been validating using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and came out with no errors. 

### JavaScript  

All **JavaScript** code has been validated using [JSHint](https://jshint.com/about/) and came out with no errors. 

### Python

All **Python** code files have been validated using [Python Code Checker](https://extendsclass.com/python-tester.html) and came out with no errors. 

## Testing User Stories 

User stories were tested in order to make sure the needs and demands of the user were met, these were the results: 

### General User

- As a general user, I want to be able to browse through all the products, and purchase the products that are to my liking.

    - Products can be viewed and purchased without the need of an account all the system in order to fullfill these actions are fully functional. 

### Un-Registered User 

- As a un-registered user, I want to be able to quickly create an account: 

    - A un-registered user can create an account using the register button located in the profile dropdown menu located in the header.

    - After creating an account users can go to their profile's page and fill in their personal information using the profile's form. This information will then be saved and transfered to the checkout page when the user is ready to make a purchase.

### Registered User

- As a registered userm I want to be able to leave reviews on products I have purchased and leave my opinion. 

    - Registered Users can access the Reviews Form from the add a review button. If a user isn't logged in they will be redirected to the sign in page. If a user is logged in they will be redirected to the Review Form where they will be able to leave a rating for that product as well as their own feedback. 

### SuperUser 

- To be able to add, delete, and edit products. 

    - If a superuser is logged in an extra navlink will be displayed where a user can Add a product by filling in the products form requirements.

    - Edit and Delete buttons with appear in the Products page allowing the user to edit and delete products. 

## Manual Testing 
### Common Feature Testing 

- All products are displaying and the correct products are displaying in the correct categories. 

- The Search Product Function Works as intended

- Quantity buttons work as intended and the add to bag button adds the product to the cart. A message pops up with the information of the product that has just been added. 

- Bag page displays the correct information and allows to edit the quantity of the products as well as remove products that are no longer wanted. 

- Checkout works perfectly if the user is signed in all the saved information is displayed. Payment goes through smoothly and an e mail confirmation is sent to the user's email. 

- Reviews if the User is signed in they are redirected to the Reviews Form where they can leave a review. When the form is submitted the review is then displayed in the respective product.

- Contact Form sends an email to the Shop Owners e mail. 

- Add, Edit, and Delete Product functionalities all work. 

## Browser Validation

The website was tested on all the following browsers and worked flawlessly:

- **Google Chrome**

- **Safari**

- **Mozilla Firefox**

- **Opera GX**