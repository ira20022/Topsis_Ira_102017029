### Topsis_Ira_102017029
_for: **TOPSIS**_
_submitted by: **Ira Vashisht**_
_Roll no: **102017029**_
_Group: **COPC2**_


TOPSIS_Ira_102017029 is a Python library for (TOPSIS).The Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) method determines the best solution from a set of alternatives with certain attributes. The best alternative is chosen based on its Euclidean distance from the ideal solution. TOPSIS is widely used in various multi-attribute decision making problems such as supply chain logistics, marketing management, environmental management or chemical engineering. Despite the extensive use of this method, there is no free and open-source software (FOSS) for TOPSIS with comprehensive post-analysis extensions

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Topsis-Ira-102017029.



## Usage

Enter csv filename followed by _.csv_ extentsion, then enter the _weights_ vector with vector values separated by commas, followed by the _impacts_ vector with comma separated signs _(+,-)_

### INPUT
And using this package in Python as :

```bash
import Topsis_Ira_102017029.topsis as tp
a =[
     [250, 16, 12, 5],
     [200, 16, 8, 3],
     [300, 32, 16, 4],
     [275, 32, 8, 4],
     [225, 16, 16, 2]
   ]
w = [0.25, 0.25, 0.25, 0.25]
sign = [-1, 1, 1, 1]
tp.topsis(a, w, sign)
```

The package can be used via commandline as :
```bash
$ python [package name] [path of csv as string] [list of weights as string] [list of sign as string]
```
## Example

#### sample.csv

A csv file showing data for different mobile handsets having varying features.

| Model  | Storage space(in gb) | Camera(in MP)| Price(in $)  | Looks(out of 5) |
| :----: |:--------------------:|:------------:|:------------:|:---------------:|
| M1 | 16 | 12 | 250 | 5 |
| M2 | 16 | 8  | 200 | 3 |
| M3 | 32 | 16 | 300 | 4 |
| M4 | 32 | 8  | 275 | 4 |
| M5 | 16 | 16 | 225 | 2 |

weights vector = [ 0.25 , 0.25 , 0.25 , 0.25 ]

impacts vector = [ + , + , - , + ]


### Output:


| Model  | Storage space(in gb) | Camera(in MP)| Price(in $)  | Looks(out of 5) | Topsis Score | Rank |
| :----: |:--------------------:|:------------:|:------------:|:---------------:|:------------:|:-----:|
| M1 | 16 | 12 | 250 | 5 |  0.534277 | 3 |
| M2 | 16 | 8  | 200 | 3 |  0.308368 | 5 |
| M3 | 32 | 16 | 300 | 4 |  0.691632 | 1 |
| M4 | 32 | 8  | 275 | 4 |  0.534737 | 2 |
| M5 | 16 | 16 | 225 | 2 |  0.401046 | 4 |




