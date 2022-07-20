# Python Standard Data Types

Run each commands and try to understand each data type and its operation.

## Numbers

### Practice 1: Numbers and oparators

`2 + 2`

`10 / 4`

`50 - 5*6`    

`(50 - 5)*6`

`5 ** 2`       

`7 % 2`

`7 // 2`

`3.14 + 2`

Assign the integer 20 to the variable `width`

Assign the float 5 to the variable `height`

Save `width * height` to the variable `area`

What is the area?

What happens if you assign 30 to `width` and print `area` again?  

Re-assign `width * height` to `area` and see if the results changes now.  

Assign `area * 2` to `2timesArea`

Assign `area + 2` to `return`

#### Answers

2 + 2

3.14 + 2

So why is the example above not 5.14? Python represents floats as base 2 (binary) fractions. This causes some of the numbers to having to be approximated instead of exact. If you need very precise calculations you need to be aware that python behaves this way. To read more about this, click [here](https://docs.python.org/3/tutorial/floatingpoint.html)

### Practice 2: Input

Assign `width` and `height` from Keyboard and calculate the `area`.

#### Answers

## Strings

### Practice 1: Strings and operators

`'Hello World!'`  
`"Hello World!"`

`'Oh, no, you didn\\'t...'`  
`"Oh, no, you didn't..."`

`"\\"Yes\\", I did!"`  
`'"Yes", I did'`


`'Hello'     '  '   'World'     '!'`

`s = 'Hello\tWorld'`  
`s`         
`print(s)`  


`s = 'First line.\nSecond line.'`  
`s`  
`print(s)`  

`folder = 'C:\some\name'`  
`print(folder)`  

`folder = r'C:\some\name'`  
`print(folder)`  

`'hmm ' + 3 * 'miam'`  

`'Py' 'thon'`  

`prefix = 'Py'`  
`prefix + 'thon'`  

`text = ('Put several strings within parentheses ' +`  
&emsp;&emsp;&emsp;&emsp; `'to have them joined together, ' +`  
&emsp;&emsp;&emsp;&emsp; `'with the use of ' +`  
&emsp;&emsp;&emsp;&emsp; `'concatenation')`  
`text`

#### Answers

### Practice 2: String formats

`pi = 3.14`

`'pi number is {}'.format(pi)`

`'Mot hai ba 4 {1} {0} {1}'.format('one', 'two')`

`g = 0.156789`

`print('Doanh so tang {:.2%}'.format(g))`

`'{:*>10}'.format('test')`

`'{:*<10}'.format('test')`

`'{:.3f}'.format(1.2345)`

`'{pi:#.2f}'.format(pi = 3.14159265359)`

`'{pi: ^ #12,.2f}'.format(pi = 10003.14159265359)`

`'{:.1%}'.format(0.156)`

`a = 123.4567
b = 456
'abcdef {:.1%} and {:.1%}'.format(a, b)`

`a = 123.4567
b = 456
f'abcdef {a:.1%} and {b:.1%}'`

#### Answers

See more about pyformat at:
[https://pyformat.info/](https://pyformat.info/)

### Practice 3: String slicing

`s = 'Data Python'`

`s[:4]`

`s[5:9]`

`s[-5:]`

`s[-1:-6:-1]`

`s[::-1]`

#### Answers

s[start:stop:step]

## Boolean

`1 == 2`

`1 < 2`

`a, b, c, d = 3, 2, 1, 4`

`(a > b) and (b > c)`

`a > b > c > d`

`bool('')`

`bool(' ')`

`bool(None)`

`bool(1)`

`bool(0)`

`bool(0.1)`

`bool([1, 2, 3])`

`bool([])`

#### Answers

## Date and times

The built-in Python datetime module provides datetime, date, and time types. The
datetime type, as you may imagine, combines the information stored in date and
time and is the most commonly used:
See more at: [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

from datetime import datetime, date, time

### Practice 1: Datatime object

`dt = datetime(2018, 9, 12, 2, 34, 12)`

`dt`

`dt.day`

`dt.hour`

`dt.date()`

`dt.time()`

`dt2 = datetime.now()
dt2`

`time_delta = dt2 - dt`

`time_delta.days`

`dt + time_delta`

`time_delta.total_seconds()`

#### Answers

### Practice 2: Format datetime

`str_date_time = '11/8/2018 12:18:00 PM'
date_1 = datetime.strptime(str_date_time, '%m/%d/%Y %I:%M:%S %p')
date_1`

`sample_date  = datetime(2018, 11, 8, 12, 18)
s_date = sample_date.strftime('%m/%d/%Y %I:%M:%S %p') 
s_date`

`curent_date = date.today()`

`curent_date.strftime('%d-%m-%Y')`

`curent_date.strftime('%A %d-%B-%Y')`

#### Answers

See more datetime format at: [https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
