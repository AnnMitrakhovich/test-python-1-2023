import pandas as pd

import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)

final_data = pd.get_dummies(data["whoAmI"]).astype(int)
print(final_data)

#def hot_encoding_without_get_dummies():