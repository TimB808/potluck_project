import os
import numpy as np

################# Variable #################
PROJECT_ID = 'PRODUCT_ID_HERE!' # Please fill this out
DATA_SIZE = "50" # num of rows ['50', '10000', 'all']
# Other variables might be put in place

################# Constants #################
LOCAL_DATA_PATH = os.path.join(os.path.expanduser('~'), "potluck_project")
#LOCAL_REGISTRY_PATH =  os.path.join(os.path.expanduser('~'), "potluck_project", #PUT SOME OTHER SUBFOLDERS HERE IF YOU LIKE

#COLUMN_NAMES_RAW = [''] # ONLY IN THE CASE OF MAKING A BigQ!

#DTYPES_RAW = {} # PLEASE CHECK COLUMN NAMES AND SEE THEIR DTYPES

DTYPES_PROCESSED = np.object
