import pandas as pd

data = pd.read_json('https://jsonplaceholder.typicode.com/todos/')


print(data.info)


