import sys
import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import data
from modules import dk_module as dk
from modules import lwl_module as lwl
from modules import nst_module as nst
from modules import vegas_module as vegas
from helpers import utils
from helpers import urls
load_dotenv()
SPORT_ID = 3
GAME_TYPE = 'Classic'
def main():
    print(f"Sport ID: {SPORT_ID}")
    print(f"Game Type: {GAME_TYPE}")
if __name__ == "__main__":
    main()