# Combine all module funs together
from logic.params import *
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
from google.cloud import bigquery
from pathlib import Path


def process_train(GCP_PROJECT, LOCAL_DATA_PATH):
    query = f"""
        SELECT {",".join(COLUMN_NAMES_RAW)}
        FROM {GCP_PROJECT}.{BQ_DATASET}
        """
    data_query_cache_path = Path(LOCAL_DATA_PATH).joinpath("raw_data", f"query_{name}_{steps}_{ingredients}.csv")
    data_query_cached_exists = data_query_cache_path.is_file()
    if data_query_cached_exists:
        data = pd.read_pickle(data_query_cache_path)
    else:
        client = bigquery.Client(project=GCP_PROJECT)
        query_job = client.query(query)
        result = query_job.result()
        data = result.to_dataframe()

        data.to_pickle(data_query_cache_path, header=True, index=False)

    return data
