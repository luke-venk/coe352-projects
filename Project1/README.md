# Project 1
## Inputs
In order to modify the inputs, navigate to `Project1/inputs` and modify the following files:  
1. masses.txt  
2. springs.txt  

The first line of the input files should be the number of masses/springs. Each following input should be the spring constant or mass of the object. The units should be in N/m for spring constants or kg for masses.

## Running the Script
To install all the dependencies needed for this project, run the following command:  
`pip install -r requirements.txt`

If you would like to run your own inputs, just populate the numbers in the `Project1/inputs/` directory. Navigate to `Project/` and run the following command:  
`python3 spring_system.py`  

By leaving the command line arguments empty, the inputs in the `inputs` directory will be used. If you would rather use given inputs for either a fixed-fixed system or a fixed-free system, run the following commands:  
`python3 spring_system.py --type fixed_fixed`  
`python3 spring_system.py --type fixed_free`  