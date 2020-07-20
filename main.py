from visualize import *

f1 = open("coin_data.csv", "r")
# we have data from top ten cryptocurrencies over time
# will mainly just use this for closing price since they add extra commas for market cap and volume
#Currency,Date,Open,High,Low,Close,Volume,Market Cap



f2 = open("top_crypto.csv","r")
#this is data from top 1500 cryptocurrencies at one point in time
#will use this to compare market caps and other things
#Number,Name,Symbol,Market Cap,Price,Circulating Supply,Volume (24hr), 1h, 24h, 7d


#the first dict will be of data and price for a cryptocurrency
dict1 = {}
prices = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
  ]
  
#second file dictionary - this will contain coin and market cap pairings
dict2 = {}
#also from second file- this will contain coin and volume over a day period
dict3 = {}

startdates = []
enddates = []
enddates.append("Apr 24 2019")
i = 0
name = ""
for line in f1:
  if line != "":
    line = line.strip()
    data1 = line.split(",")
    if data1[6] != "Volume":
      price = float(data1[6])
    if len(prices[i]) > 3 and i == 0 and data1[0] != name:
      startdates.append(date)
      enddates.append(data1[1]+data1[2])
      i=1
      dict1[name] = prices[0]
    elif data1[0] not in dict1 and i != 0 and name != data1[0] and len(prices[i])>1:
      startdates.append(date)
      enddates.append(data1[1]+data1[2])
      dict1[name] = prices[i]
      i += 1
    if data1[6] != "Volume":
      prices[i].append(price)
    name = data1[0]
    date = str(data1[1]+data1[2])
    if i == 9 and price == 0.024969:
      startdates.append(data1[1]+data1[2])
      dict1[name] = prices[i]

#now we have a dictionary with the name of a crypto and a list of prices through time starting most recently

for line in f2:
  if line != "":
    line = line.strip()
    data2 = line.split(",")
    name = data2[1]
    if data2[3] != "?":
      marketcap = float(data2[3])
      dict2[name] = marketcap
    if data2[6] != "":
      volume = float(data2[6])
      dict3[name] = volume

# we now have two dictionaries to represent 1500 cryptos and their marketcap/volume



top10 = list(dict1.values())

#will now sort based on time
#need to reverse lists
for i in range(len(top10)):
  top10[i] = list(reversed(top10[i]))

#ten figures for top ten cryptocurrencies
h1 = figure(title = "Price of Ripple through time")
h2 = figure(title = "Price of Binance Coin through time")
h3 = figure(title = "Price of EOS through time")
h4 = figure(title = "Price of Bitcoin through time")
h5 = figure(title = "Price of Tether through time")
#interesting since tether is pegged to US dollar
h6 = figure(title = "Price of Bitcoin Cash through time")
h7 = figure(title = "Price of Stellar Lumens through time")
h8 = figure(title = "Price of Litecoin through time")
h9 = figure(title = "Price of Ethereum through time")
h10 = figure(title = "Price of Cardano through time")

#first I will show a plot of the coins vs time; bar chart or line chart work fine
#unused code for bar chart that also works (I found line chart to run faster):
#for i in range(len(top10[0])):
  #h1.vbar(i+1,.95,top10[0][i],0)
  

lencoins = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
  ]
  
for i in range(len(top10)):
  for j in range(len(top10[i])):
    lencoins[i].append(j)
  
linechart(lencoins[0],top10[0],"blue",h1)
h1.text(0, 0, [startdates[0]])
h1.text(len(top10[0])-300, 0, [enddates[0]])
h1.yaxis.axis_label = "price in $"
h1.xaxis.axis_label = "days since start date"

linechart(lencoins[1],top10[1],"blue",h2)
h2.text(0, 0, [startdates[1]])
h2.text(len(top10[1])-120, 0, [enddates[1]])
h2.yaxis.axis_label = "price in $"
h2.xaxis.axis_label = "days since start date"

linechart(lencoins[2],top10[2],"blue",h3)
h3.text(0, 0, [startdates[2]])
h3.text(len(top10[2])-120, 0, [enddates[2]])
h3.yaxis.axis_label = "price in $"
h3.xaxis.axis_label = "days since start date"

linechart(lencoins[3],top10[3],"blue",h4)
h4.text(0, 0, [startdates[3]])
h4.text(len(top10[3])-320, 0, [enddates[3]])
h4.yaxis.axis_label = "price in $"
h4.xaxis.axis_label = "days since start date"

linechart(lencoins[4],top10[4],"blue",h5)
h5.text(0, 0, [startdates[4]])
h5.text(len(top10[4])-300, 0, [enddates[4]])
h5.yaxis.axis_label = "price in $"
h5.xaxis.axis_label = "days since start date"

linechart(lencoins[5],top10[5],"blue",h6)
h6.text(0, 0, [startdates[5]])
h6.text(len(top10[5])-120, 0, [enddates[5]])
h6.yaxis.axis_label = "price in $"
h6.xaxis.axis_label = "days since start date"

linechart(lencoins[6],top10[6],"blue",h7)
h7.text(0, 0, [startdates[6]])
h7.text(len(top10[6])-300, 0, [enddates[6]])
h7.yaxis.axis_label = "price in $"
h7.xaxis.axis_label = "days since start date"

linechart(lencoins[7],top10[7],"blue",h8)
h8.text(0, 0, [startdates[7]])
h8.text(len(top10[7])-300, 0, [enddates[7]])
h8.yaxis.axis_label = "price in $"
h8.xaxis.axis_label = "days since start date"

linechart(lencoins[8],top10[8],"blue",h9)
h9.text(0, 0, [startdates[8]])
h9.text(len(top10[8])-300, 0, [enddates[8]])
h9.yaxis.axis_label = "price in $"
h9.xaxis.axis_label = "days since start date"

linechart(lencoins[9],top10[9],"blue",h10)
h10.text(0, 0, [startdates[9]])
h10.text(len(top10[9])-100, 0, [enddates[9]])
h10.yaxis.axis_label = "price in $"
h10.xaxis.axis_label = "days since start date"

#show(h1)
#show(h2)
#show(h3)
#show(h4)
#show(h5)
#show(h6)
#show(h7)
#show(h8)
#show(h9)
#show(h10)
#these are all the charts for top ten cryptos through time


  

#bar chart market cap
names = list(dict2.keys())
names.sort(key = lambda x:dict2[x], reverse = True)

#for practicial purposes I'll show top 30
g1 = figure(title = "Top market caps")
for i in range(30):
  g1.vbar(i+1,.95,dict2[names[i]],0)
  g1.text(i+1.5, 0, [names[i]],math.pi/2)
g1.yaxis.axis_label = "Market Cap in $"
#show(g1)

#this will be a piechart of market caps showing top 3 and all other cryptos
g2 = figure(title = "Market Capitalization",x_range = (0,8), y_range = (0,10))

cap = [dict2[names[0]],dict2[names[1]],dict2[names[2]]]
sum1 = 0
for i in range(len(names)):
  if i >2:
    sum1 += dict2[names[i]]
cap.append(sum1)
names2 = names[0:3]
names2.append("other")
pieChart(cap,names2,["blue","green","black","red"],3,5,g2)
#show(g2)


#final graph is bar chart by volume
names2 = list(dict3.keys())
names2.sort(key = lambda x:dict3[x], reverse = True)
k = figure(title = "Top 30 cryptocurrencies by volume")
#define axes
for i in range(30):
  k.vbar(i+1,.95,dict3[names2[i]],0)
  k.text(i+1.5, 0, [names2[i]],math.pi/2)
k.yaxis.axis_label = "volume in $"
show(k)

'''
That wraps up this project! All in all there are 13 graphs/charts, with ten showing
the prices of the top ten cryptocurrencies throughout time, and the last three showing
the top cryptocurrencies by market cap and volume, as well as a look at the overall bitcoin
dominance in the market.
In the future I would be interested in using this format with a continuously updating dataset
Afterall, that is how websites like coinmarketcap essentially do exactly what I do here!
This might be possible by getting live data from all the different exchanges...
But in essence this program provides many useful utilities for graphing data on cryptocurrencies!
'''

