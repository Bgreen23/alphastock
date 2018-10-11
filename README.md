Discover/Requirements
  Need stock data from different companies
  We need the data to show our client what stocks to invest in
  Short term vs long term investments(Weekly vs Monthly vs Yearly)

Collection
  Using data from alphavantage.co
    https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=MSFT&apikey=demo&datatype=csv
    https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=AAPL&apikey=demo&datatype=csv
    https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=DIS&apikey=demo&datatype=csv
    https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=NVDA&apikey=demo&datatype=csv
    https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=SNE&apikey=demo&datatype=csv

Data Prep/Cleaning
  The data that I grab from alphavantage had both short term(weekly) as well as long term(monthly + yearly) data. From here I had to decide on where to trim the data.

Exploration/Planning
  I decided to do a short term investment strategy instead of a long term investment. I picked the month of September because it was the closest month to October with a full dataset.

Modeling/Algorithms
  I decided to make two line graphs that show the weekly highs and lows in the month of September.

Automation/Computation
  I used matplotlib to make line graphs because it seemed to be the easiest method to get the desired results.

Findings/Review/Repeat
  Nvidia is the best short term investment because of it's high risk/reward. The lowest price in the month of September was $258.68 while the highest was $285.22. That's a difference of around $26-$27. If you're looking for long term investments I can put together visualizations that show the long term trends of these 5 companies but for now, I would look into a short term investment in Nvidia.
