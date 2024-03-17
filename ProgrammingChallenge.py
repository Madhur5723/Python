'''Programming Challenge: Grocery Store Purchase
A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:

Penne 16 oz Pack of 12 - $16.68

Arrabiata Pasta Sauce 24 oz - $6.98

Bag of 20 Organic Garlic Cloves - $16.78

Italian Seasoning 1.5 oz Bottle - $15.26

Artisan Baguettes Twin Pack - $3.00

12 oz Bag of Meatballs - $4.39

In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  The subtotal is just the sum of all of their prices.

Use print() to display the result of the expression. 
'''

# Variables holding the prices of the six items:
 
# All of the variables were multiplied by 100 to make them into integers so that there would be no approximation errors
# when they were added together.
 
pasta = 16.68 * 100  
sauce = 6.98 * 100  
garlic = 16.78 * 100 
seasoning = 15.26 * 100  
bread = 3.00 * 100  
meatballs = 4.39 * 100  
subtotal = (pasta + sauce + garlic + seasoning + bread + meatballs) / 100
print(subtotal)