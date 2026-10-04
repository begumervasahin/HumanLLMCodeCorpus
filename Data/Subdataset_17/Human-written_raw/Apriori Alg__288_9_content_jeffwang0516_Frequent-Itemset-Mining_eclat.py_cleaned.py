9. Repository: jeffwang0516/Frequent-Itemset-Mining
   File: eclat.py
   URL: https:
   Code Content:
import sys
import time
from association_rules.frequent_itemset_mining import Eclat
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Please use correct args!")
        sys.exit()
    input_file = sys.argv[1]
    min_support_ratio = float(sys.argv[2])
    output_file = sys.argv[3]
    eclat = Eclat(use_data_struc='np_bit_array')
    eclat.proccess_input_data(input_file)
    print("[Eclat] Finding freq Itemset with min support >",
          min_support_ratio, '--')
    start_time = time.time()
    eclat.find_supersets_k(min_support_ratio)
    eclat.save_output(output_file)
    end_time = time.time()
    print("Elapsed time =", end_time-start_time)
    print('----------\n')
   README Content:
[![Total alerts](https:
Implementation of Apriori and Eclat
- python 3.6
```sh
$1: input file
$2: min support ratio (0 < $2 < 1)
$3: output file
```
- Apriori
  ```sh
  $ bash apriori.sh $1 $2 $3
  ```
- Eclat
  - CPU
    ```sh
    $ bash eclat_cpu.sh $1 $2 $3
    ```
  - GPU
    ```sh
    $ bash eclat_gpu.sh $1 $2 $3
    ```
![img](time_compare.png)
