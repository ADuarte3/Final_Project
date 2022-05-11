from enum import Enum

# simulation settings
POP_SIZE = 5000     # cohort population size
SIM_LENGTH = 150   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

ANNUAL_PROB_BACKGROUND_MORT = 9.1/1000


class HealthStates(Enum):

    WELL = 0
    POLYP = 1
    PRECANCER = 2
    CANCER = 3
    CANCER_DEATH = 4
    NATURAL_DEATH = 5


# transition matrix
TRANS_MATRIX = [
    [1, 0, 0, 0, 0],        # well
    [0.862, 0, 0.074, 0.064, 0],     # polyp
    [0.13, 0, 0, 0.87, 0],     # precancer
    [0, 0, 0, 0.65, 0.35]     # cancer
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0,           # Well
    892,         # Polyp/Cost of removal
    10000,       # Pre-Cancer/Cost of treatment
    60321,       # Cancer Costs
    0]           # Death


# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.00,        # Well
    0.75,        # Polyp
    0.50,        # Pre-Cancer
    0.25,        # Cancer
    0            # Death
]

# screening costs
Colonoscopy_COST = 648.52
Colonography_COST = 488.29

# relative risk
COLONOGRAPHY_RR = 0.0004
