# Project 1
## Setup
Create virtual environment:  
`python -m venv venv`  
`source venv/bin/activate`  

To install all the dependencies needed for this project, run the following command:  
`pip install -r requirements.txt`

## Part 1
The `svd_calculator.py` script is used to solve part 2. If you really want to call the script on a custom matrix A, just define A in the file below the function and call the function.  

## Part 2
### Inputs
In order to modify the inputs, navigate to `Project1/inputs` and modify the following files:  
1. masses.txt  
2. springs.txt  

The first line of the input files should be the number of masses/springs. Each following input should be the spring constant or mass of the object. The units should be in N/m for spring constants or kg for masses. You can see the examples in the `fixed_fixed_inputs` or `fixed_free_inputs` directories.

### Running the Script
If you would like to run your own inputs, just populate the numbers in the `Project1/inputs/` directory. Navigate to `Project/` and run the following command:  
`python3 spring_system.py`  
By leaving the command line arguments empty, the inputs in the `inputs` directory will be used. Based on the number of springs and masses in the input files, the program will know whether to solve a fixed-fixed or a fixed-free spring-mass system of equations.

If you would rather use some example inputs for either a fixed-fixed system or a fixed-free system, run the following commands:  
`python3 spring_system.py --type fixed_fixed`  
`python3 spring_system.py --type fixed_free`  