
import pandas as pd

# Create a DataFrame from List of Dicts
data = [{'elma': 1, 'armut': 2}, {'karpuz': 5,
                                  'armut': 10, "elma": 20}, {"aaa": 11, "bbb": 22}]
print(type(data))
print(type(data[0]))

print("---------------------------------------------------")
df = pd.DataFrame(data)
print(df)
print("---------------------------------------------------")
