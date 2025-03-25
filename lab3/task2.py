import re

def sum_monetary_amounts(text):
    amounts = re.findall(r'\$\d+\.?\d*', text)
    
    float_amounts = [float(amount[1:]) for amount in amounts]
    
    return sum(float_amounts)

text = "first amount is $123.45, second amount is $400"
print(sum_monetary_amounts(text)) 