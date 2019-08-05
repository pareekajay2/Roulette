# Problem Statement
The program that I'd like you to build is called ProductRoulette. It can be a command-line tool. A user enters her email and persona (developer, salesperson, marketing, hr, engineering manager, etc.), and the program immediately starts showing interesting B2B products that she may or may not like to adopt at her company. Depending on the feedback (we can play around with what we seek as feedback but it needs to be unobtrusive and non-lengthy), the program gets progressively smarter and gets the user's stack interest profile. This Interest/Taste graph can also be used for the next user, creating a network effect. Like a Tinder/Netflix for Software Products.

# Solution
Store details of users in the users table.

A products table for details of the product.

Feedback table for storing data of a user providing feedback on a particular product.

To provide suggestions to a user, people with same persona's data will be taken and the top 5 products for them will be recommended. The top 5 products will regularly get updated with increase in reviews.

Run product.py to run the application in the terminal.

Provide the user inputs as asked.

How to run through the program: 

1. Enter whether you want to signin/signup.

2. Provide details like username and password.

3. A dataframe of top 5 products will be shown

4. Search for a product.

5. Provide ratings and review

I have added a very basic data of products in `developer` and `analytics` persona.
