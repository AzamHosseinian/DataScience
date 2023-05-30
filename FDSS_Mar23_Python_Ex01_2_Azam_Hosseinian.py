from collections import Counter
from tabulate import tabulate

frequency = Counter(input("Please enter a text: ").replace(" ", ""))
print(tabulate(frequency.items(), headers = ['CHARACTER', 'FREQUENCY'], tablefmt = 'pipe'))
