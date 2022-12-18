import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
Database = "aps_fault"
Collection = "sensor"

if __name__=="__main__":
    df = pd.read_csv("/config/workspace/aps_failure_training_set1.csv")
    print(f"Rows and Columns : {df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[Database][Collection].insert_many(json_record)