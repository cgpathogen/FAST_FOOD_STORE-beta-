# FAST_FOOD_STORE
Simple python code for online fast food cafe (user can place an order of noodles, burger and drinks), protected from most of ValueErrors. 
Before placing an order user must pass registration. User can either place a full order of noodles, burger and drinks or partially choose and order one or two goods from the list. 
There's a constructor of burger in this code. User can choose amount of ingredients that they need (total amount is 9 and each ingredient has its own price) and construct their own burger. 
If a user is younger 18 y.o. they won't be able to order a beer.
After choosing a good user can skip an order pressing 0 when the system offers them to choose amount of ordered good.
User can skip choosing of a good by pressing 0, in this case they'd be offered another good. 
If user places an empty order by pressing 0 for any offered good, total price of order will be equal 0. 
All cases when exactly int or str must be used in inputs are protected by try/except construction to avoid ValueErrors.
User can use a promocode. In this case total price will be 7% off.

p.s.

Well, i should have used functions instead of some repeated blocks of code, but i'm still not so experienced in using functions :)) 
I'm workig on it.
