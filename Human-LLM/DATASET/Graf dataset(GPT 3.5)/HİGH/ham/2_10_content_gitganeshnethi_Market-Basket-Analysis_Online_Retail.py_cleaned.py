10. Repository: gitganeshnethi/Market-Basket-Analysis
   File: Online_Retail.py
   URL: https:
   Code Content:
import pandas as pd
import numpy as np
from apyori import apriori
b1 = pd.read_excel('D:\\ML-Class\\Data Sets\\Apriori\\Online Retail.xlsx')
b1.head()
b2 = b1[b1['Country']=='France']
b2.shape
b3 = b2.iloc[:,[0,2]]
b4 = []
for i in b3['InvoiceNo'].unique():
    b5 = list(b3[(b3['InvoiceNo'] == i)]['Description'])
    b4.append(b5)
b6 = apriori(b4,min_support = 0.05,
                             b7 = 0.2, min_lift = 3,
                             b8 = 3)
b9 = list(b6)
len(b9)
b9[1]
b10 = pd.DataFrame()
for i in b9:
    b11 = i
    b12 = {'Base_item':b11[2][0][0],
                'Add_item':b11[2][0][1],
                'Confidence':b11[2][0][2],
                'lift':b11[2][0][3]}
    b10 = b10.append(b12,ignore_index=True)
b10.head(10)
   README Content:
<h2><i><u>Market-Basket-Analysis</></i></h2>
- Market Basket Analysis using Apriori Algorithm
<b11 b13 = 'https:
<h3>Purpose :</h3>
<p><b>When get an oppurtunity on retail project where your problem statement is to improve store performance regarding sales and reduce store inventory, in such cases Market Basket Analysis is the technique that gives best b9.</b></p>
<ol>
<b4>Market basket Analysis allows retailers to know the relationship or association between items which are more frequently bought together</b4>
<b4>Can be implemented using technique called Apriori Algorithm</b4></ol>
<b>By looking into this example let us understand how it is done</b>
 * Imagine we have transactions of <b>n</b> customers who purchased something from retail store</b4>
 * Transactions are like this...
 <p> Customer 1: Bread, egg, papaya, oats</p>
 <p> Customer 2: Papaya, bread, oat packet and milk</p>
 <p> Customer 3: Egg, bread, and butter</p>
 <p> Customer 4: Oat packet, egg, and milk</p>
 <p> Customer 5: Milk, bread, and butter</p>
 <p> Customer 6: Papaya and milk</p>
 <p> Customer 7: Butter, papaya, and bread</p>
 <p> Customer 8: Egg and bread</p>
 <p> Customer 9: Papaya and oat packet</p>
 <p> Customer 10: Milk, papaya, and bread</p>
 <p> Customer 11: Egg and milk</p>
 <p> .             .</p>
 <p> .             .</p>
 <p> .             .</p>
 <p> Customer n    .</ul></p>
<b>Observe through the transactions that three customers have bought bread and butter, the technique will tell us that if bread is bought then there is high chance that same customer also bought butter.</b>
<p>Generally this technique gives best patterns for retailers to promote and cross-sell their items in store.</p>
<ol>
<p>Three metrics in finding these association b9 are</p>
<b4>Support</b4>
<b4>Confidence</b4>
<b4>b14</b4></ol>
<h4>Support :</h4>
<p>Support is the minimum probability for the product to get sold. Percentage of orders that contain the item set is explained</p>
<b> Support{x} = freq(x)/n </b> [x --> item, n --> total no of transactions]
<h4>Confidence :<h4>
<p>Given two items x,y confidence measure the percentage of times that item y is purchased, given that x was purchased</p>
<p>Confidence Value always ranges between 0 and 1. Where 0 indicates y is never purchased when x is purchased</p>
<p>1 indicates y is always purchased whenever x is purchased</p>
<b> Confidence{x,y} = freq(x,y)/freq(x)</b>
<h4>b14 :</h4>
<p>This is unlike confidence metric whose value may vary depending on direction</p>
Example : Confidence{x,y} is different from Confidence{y,x}
<p>b14 has no direction, which means <b>lift{x,y} = lift{y,x}</b></p>
<b>b14{x,y} = support{x,y}/(support{x}*support{y}) </b>
<ul>
  <b4>When b14 = 1; implies no relationship between x and y i.e., x and y occur together only by chance</b4>
  <b4>When b14 > 1; implies there is positive relationship between x and y i.e., x and y occur together more offer than random</b4>
  <b4>When b14 < 1; implies there is negative relationship between x and y i.e., x and y occur less often and random</b4></ul>
<img b15 = 'http:
