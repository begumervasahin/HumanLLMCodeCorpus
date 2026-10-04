9. Repository: jeffwang0516/Frequent-Itemset-Mining
   File: b5.py
   URL: https:
   Code Content:
import sys
import b8
from association_rules.frequent_itemset_mining import Eclat
if b1 = = '__main__':
    if len(sys.argv) != 4:
        print("Please use correct args!")
        sys.exit()
    b2 = sys.argv[1]
    b3 = float(sys.argv[2])
    b4 = sys.argv[3]
    b5 = Eclat(use_data_struc='np_bit_array')
    b5.proccess_input_data(b2)
    print("[Eclat] Finding freq Itemset with min support >",
          b3, '--')
    b6 = b8.b8()
    b5.find_supersets_k(b3)
    b5.save_output(b4)
    b7 = b8.b8()
    print("Elapsed b8 = ", b7-b6)
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
