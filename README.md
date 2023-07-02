# SPC statistical process control
script that calculates process capability and process capability index for given results, target, specification limit and sample size.
Results are ploted
&nbsp;
&nbsp;

## How to install
Developed and tested in python3.10.6, on ubuntu22.04

1. Create a virtual environment (venv)
```bash
python3 -m venv venv
```

2. Activate the virtual environment (you need to repeat this step, and this step only, every time you start a new terminal/session):
```bash
source venv/bin/activate
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

&nbsp;
## How to run
```bash
usage: main.py [-h] -f FILE [-sl SL] [-n {1,2,3,4,5,6,7,8,9,10,11,12}]
```

```bash
python3 main.py -f ./logdata.txt
```

&nbsp;
## How to test
```bash
pytest
```

&nbsp;
## Results
![results](https://i.imgur.com/NfBCO1L.png)