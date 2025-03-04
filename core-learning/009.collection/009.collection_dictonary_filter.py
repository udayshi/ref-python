prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

lst={k:v for k,v in prices.items() if v>40}

tech_names = { 'AAPL', 'IBM', 'HPQ' }

p2 = { key:value for key,value in prices.items() if key in tech_names } #{'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}
print(p2)

