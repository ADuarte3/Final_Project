from enum import Enum

# simulation settings
POP_SIZE = 5000     # cohort population size
SIM_LENGTH = 150   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

ANNUAL_PROB_BACKGROUND_MORT = 9.1/1000

class HealthStates(Enum):
    WELL = 0

    CANCER = 2
    CANCER_DEATH = 3
    NATURAL_DEATH = 4

# transition matrix
TRANS_MATRIX = []

# annual cost of each health state
ANNUAL_STATE_COST= []

# annual health utility of each health state
ANNUAL_STATE_UTILITY = []

# screening costs
Colonoscopy_COST = 3081
Colonography_COST = 439

# treatment relative risk
TREATMENT_RR =
