import pandas as pd
import numpy as np

import random
import time

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d %H:%M:%S', prop)

n_account = 10000
isins = ['a', 'b', 'c']
my_dict = {'volume':[], 'date':[], 'account':[], 'isin':[]}

for isin in isins:
    for account in range(1, (n_account+1)):
        n_trades = np.random.randint(10, 300)
        for trade in range(1, (n_trades+1)):
            my_dict['volume'].append(np.random.exponential(scale=1000))
            my_dict['date'].append(random_date("2018-01-01 00:00:00", "2020-10-01 15:15:00", random.random()))
            my_dict['account'].append(account)
            my_dict['isin'].append(isin)

df = pd.DataFrame(my_dict, columns=['account', 'date', 'volume', 'isin'])

df.loc[df['date'] <= "2020-01-01 00:00:00", 'period'] = 'V'
df.loc[df['date'] > "2020-01-01 00:00:00", 'period'] = 'B'

trades = df

my_dict = {'account': [], 'candidate': []}
for account in range(1, (n_account+1)):
    my_dict['account'].append(account)
    my_dict['candidate'].append(random.choice(['True', 'False']))

account_info = pd.DataFrame(my_dict, columns=['account', 'candidate'])
