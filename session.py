from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import os

try: 
    os.remove('data.database.sqliite')
except:
    print('no database sqlite')

engine = create_engine('sqlite:///data.database.sqlite')

