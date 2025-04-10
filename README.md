# Manny Factory

_Schedule to be submitted is_ `./submission/best_schedule.csv`

This project simulates a simplified apparel production process with three stages: **Cut**, **Sew**, and **Pack**. The goal is to optimize the production schedule based on various constraints, such as machine availability, order deadlines, and setup times. The program assigns each order to the earliest available machine per stage, ensuring no parallel processing.

The scheduler prioritizes **average lateness** before anything else.  
e.g. - for the case below the scheduler will prefer Schedule B over A.

| Schedule | Orders completed on time | Average lateness (days) |
| -------- | ------------------------ | ----------------------- |
| A        | 19                       | 4.12                    |
| B        | 10                       | 4.20                    |

### Requirements

- Python 3.8 or higher (you can download it [here](https://www.python.org/downloads/)).
- No additional packages are required. Python's standard library is sufficient.

### Setup Instructions

1. Ensure Python 3.8 or higher is installed. Check your version with:

   ```bash
   python --version
   ```

2. Navigate to the project directory:

   ```bash
   cd /manny-factory
   ```

3. The program requires the input data file `./data/orders.csv`. **Do not modify** this file.

### Running the Scheduler

To generate the best schedule:

```bash
py main.py
```

This will:

1. Log the total number of orders completed on time.
2. Log the average number of days each order is late (if any).
3. Output a file to `./results/best_schedule.csv` containing the reordered orders with the added `late_by` field showing the number of days each order is late.

### Testing the Performance of the Schedule

To test the performance of the saved schedule, run:

```bash
py test.py
```

This will:

1. Automatically read the results from `./results/best_schedule.csv`.
2. Print the same values: total orders completed on time and average days late.

### Additional Notes

- The input file `./data/orders.csv` should **not be modified**.
- The scheduling algorithm evaluates orders based on a forward scheduling approach and uses machine availability in discrete time units.
- Monte Carlo simulations can be used to test different permutations and find the best schedule that minimizes lateness.
