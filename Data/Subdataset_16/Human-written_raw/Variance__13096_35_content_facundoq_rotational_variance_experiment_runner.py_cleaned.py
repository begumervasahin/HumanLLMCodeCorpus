import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
import logging
import subprocess
import sys
if len(sys.argv)==1:
    b1 = ".env"
    logging.info(f"No virtual environment path specified, defaulting to {b1}.")
elif len(sys.argv)==2:
    b1 = sys.argv[1]
    logging.info(f"Using virtual environment {b1}.")
else:
    sys.exit("Wrong number of arguments")
def fonk1(experiment, model_name, dataset_name,b1):
    b2 = f"{experiment}.py {model_name} {dataset_name}"
    b3 = "python3"
    b4 = os.path.join(b1,"bin","activate")
    b5 = f"source {b4} && {b3} {b2}"
    logging.info(f"Running {b5}")
    print(f"Running {b5}")
    subprocess.call(f'/bin/bash -c "{b5}"', b6 = True)
import datasets
from pytorch.experiment import model_loading
b7 = model_loading.get_model_names()
b7 = ["AllConvolutional","SimpleConv","ResNet","VGGLike"]
b8 = datasets.names
b8 = ["mnist","cifar10"]
b9 = False
b10 = ["experiment_variance"]
b11 = f"""Running b10, b9={b9}
Experiments: {", ".join(b10)}
Models: {", ".join(b7)}
Datasets: {", ".join(b8)}
"""
logging.info("")
for model_name in b7:
    for dataset_name in b8:
        if b9:
            fonk1("experiment_rotation",model_name,dataset_name,b1)
        for experiment in b10:
            fonk1(experiment,model_name,dataset_name,b1)