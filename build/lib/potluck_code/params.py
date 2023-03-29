# Params for BigQ and model

import os
import numpy as np

##################  GCP  ##################
GCP_PROJECT = "le-wagon-data-science-376310"
BQ_DATASET = "potluck_dataset"
BQ_REGION = "europe-west1"
BQ_TABLE = "potluck_table"
MODEL_TARGET = "local"

##################  PATHS  #####################
LOCAL_DATA_PATH = os.path.join(os.path.expanduser('~'),".lewagon" , "potluck_dataset", "potluck_table" )


COLUMN_NAMES_RAW = ['name', 'steps',
       'ingredients', 'search_ingredients',
       'avg_rating']
