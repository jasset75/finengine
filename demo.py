import uuid
from datetime import datetime
import pandas as pd
import numpy as np
from pprint import pprint

def main():
  owner = dict(
    id=uuid.uuid4(),
    name='jasset',
    email='thatsme@jasset.me.uk'
  )

  account = dict(
    id=uuid.uuid4(),
    owner=owner['id'],
    balance=3000.00,
  )

  """
    notes = pd.Dataframe({
      'dates': ['24-09', '25-09', '26-09', '27-09', '28-09', '29-09', '30-09','01-10','02-10','03-10','04-10'],
      'data': [24, 26, 27, 28, 26,25,30,30,30,28,25],
      'result': [0,2,1,1,-2,0,5,0,0,-2,-3]
    })
  """
  columns = ('ts','order','ticker','account','op','uprice','quantity','completed','commission','tax','total')
  print_cols = ['order','ticker','op','uprice','quantity','completed','commission','tax','total']
  notes = pd.DataFrame(columns=columns)


  print(notes)

  fc = datetime.strptime('22/05/2017 8:30','%d/%m/%Y %H:%M')

  order = 1

  notes.loc[fc] = {
    'ts': fc,
    'order': order,
    'ticker':'POPULAR',
    'account': account,
    'op': 1,
    'uprice': 0.692,
    'quantity': 300,
    'completed': 0,
    'commission': 1.21,
    'tax': 2.41,
    'total': np.nan
  }

  order = 2

  fc = datetime.now()
  notes.loc[fc] = {
    'ts': fc,
    'order': order,
    'ticker':'POPULAR',
    'account': account,
    'op': -1,
    'uprice': 0.710,
    'quantity': 300,
    'completed': 225,
    'commission': 1.21,
    'tax': 2.41,
    'total': np.nan
  }
  
  notes.set_index(['ts','order'])

  pprint(owner)
  pprint(account)
  pd.options.display.max_rows = 80
  pd.set_option('display.max_columns', 300)
  print(notes[print_cols])
  print(pd.get_option("display.max_columns")) 



if __name__ == "__main__":
    # execute only if run as a script
    main()