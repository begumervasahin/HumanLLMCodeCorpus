import sys
import os
import data
import pandas as pd
import numpy as np
from modules.dk_module import *
from modules.lwl_module import *
from modules.nst_module import *
from modules.vegas_module import *
from helpers.utils import *
from helpers.urls import *
from dotenv import load_dotenv
load_dotenv()
sportId = 3
gameType = 'Classic'
def main():
    print(f"Sport ID: {sportId}")
    print(f"Game Type: {gameType}")
if __name__ == "__main__":
    main()