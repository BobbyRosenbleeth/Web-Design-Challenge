#Convert CSV to HTML using Pandas

import pandas as pd

data = pd.read_csv("Resources\cities.csv")
data = pd.DataFrame(data)

html_data = data.to_html()

with open("my_file.html", "w") as f:
    f.write(html_data)