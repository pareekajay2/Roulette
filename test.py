import sqlite3
import pandas as pd
import uuid
import datetime
from database import update_user_data, insert_feedback
DB = "product-roulette.db"

insert_feedback(id=str(uuid.uuid4()), )