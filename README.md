Cheapest Route Planner
========

This is a candidate solution for the term project of COMP20230.
See projecthandout.pdf for project specifications.
See 17205389_DSTermProject.pdf for report on the solution.


Prerequisites
----------------------

This project was created in a Python 3.6 environment. It will be easier to set up the project if you install [Anaconda](https://conda.io/docs/user-guide/install/download.html) or [Miniconda](https://conda.io/miniconda.html). Other options, such as [PyEnv](https://github.com/pyenv/pyenv) and classic virtual environment (i.e. `venv`), will also work.


Installation and Setup
----------------------

Run the following commands in Terminal:

```sh
git clone https://github.com/obyrned1/COMP20230_DataStructures-Algorithms_TermProject.git 
conda env create -f environment.yml
pip install -r requirements.txt
```

Running the Program
-------------------

From the project directory (in Terminal), run this command:

```sh
python main.py 
```

Running the Tests
------------------

From the project directory (in Terminal), run these commands to test the main, Aiport, Currency and Aircraft classes:

```sh
py.test --verbose testMain.py
	- To run the testMain.py file, you must uncomment the "return data" statement at the end of the main.py file
	- Then comment this line when you want to run the main.py file
py.test --verbose testAirport.py
py.test --verbose testCurrency.py
py.test --verbose testAircraft.py

```
