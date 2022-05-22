# Yahoo! Earnings Calendar Scraper

> 项目从 https://github.com/wenboyu2/yahoo-earnings-calendar 修改而来，增加 yahoo Finance数据解析(历史数据怎么获取我也不知道)，个人更喜欢dataframe的返回，所以将返回都改为pandas的dataframe


## Usage

### Get Financials data

```py
import datetime
from yahoo_earnings_calendar import YahooEarningsCalendar
yfs = YahooFinancialsStmt()
yfs.get_financials('box')
```

### Get earnings date information on a specific date or in a date range
```python
import datetime
from yahoo_financials_stmt import YahooFinancialsStmt

date_from = datetime.datetime.strptime(
    'May 5 2017  10:00AM', '%b %d %Y %I:%M%p')
date_to = datetime.datetime.strptime(
    'May 8 2017  1:00PM', '%b %d %Y %I:%M%p')
yfs = YahooFinancialsStmt()
print(yfs.earnings_on(date_from))
print(yfs.earnings_between(date_from, date_to))
```



### Get the next earnings date of a specific symbol
```python
import datetime
from yahoo_financials_stmt import YahooFinancialsStmt

yec = YahooFinancialsStmt()
# Returns the next earnings date of BOX in Unix timestamp
print(yfs.get_next_earnings_date('box'))
# 1508716800
```

### Get all the available earnings data of a specific symbol
```python
from yahoo_financials_stmt import YahooFinancialsStmt

yfs = YahooFinancialsStmt()
    # Returns a list of all available earnings of BOX
print(yec.gfs_earnings_of('box'))
```


