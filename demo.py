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
  )

  """
    notes = pd.Dataframe({
      'dates': ['24-09', '25-09', '26-09', '27-09', '28-09', '29-09', '30-09','01-10','02-10','03-10','04-10'],
      'data': [24, 26, 27, 28, 26,25,30,30,30,28,25],
      'result': [0,2,1,1,-2,0,5,0,0,-2,-3]
    })
  """

  notes = pd.DataFrame(columns=('ts','ticker','op','uprice','quantity','commission','taxe','total'))


  print(notes)

  fc = datetime.strptime('22/05/2017 8:30','%d/%m/%Y %H:%M')
  notes.loc[fc] = {
    'ts': fc,
    'ticker':'POPULAR',
    'op': 1,
    'uprice': 0.692,
    'quantity': 300,
    'commission': 1.21,
    'taxe': 2.41,
    'total': np.nan
  }

  fc = datetime.now()
  notes.loc[fc] = {
    'ts': fc,
    'ticker':'POPULAR',
    'op': -1,
    'uprice': 0.710,
    'quantity': 300,
    'commission': 1.21,
    'taxe': 2.41,
    'total': np.nan
  }
  
  notes.set_index('ts')

  pprint(owner)
  pprint(account)

  print(notes)

if __name__ == "__main__":
    # execute only if run as a script
    main()