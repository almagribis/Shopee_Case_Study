from uuid import uuid4
import pandas as pd
import random, re
from PIL import Image
from datetime import datetime, timedelta


def get_date_and_time():
    timezone = get_timezone()
    times_area = get_time_area(timezone)
    return times_area

def get_session_id():
    session_id = str(uuid4())
    return session_id

def build_data_table(raw_data):

    documents = []
    for data in raw_data:
        documents.append(
            {
                "no": data["no"],
                "title": data["title"],
                "source": data["source"],
                "last_updated": data["last_updated"].strftime("%Y-%m-%d %H:%M:%S"),
                "Ready For Conversation": "✅",
            }
        )

    if len(documents) == 0:
        documents.append(
            {
                "no": "No Data",
                "title": "No Data",
                "source": "No Data",
                "last_updated": "No Data",
                "Ready For Conversation": "No Data",
            }
        )

    df = pd.DataFrame(documents)
    return df