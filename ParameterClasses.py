from enum import Enum
import numpy as np
import InputData as Data
from InputData import HealthStates
import SimPy.Markov as Markov


class Therapies(Enum):
    """ colonoscopy vs. colonography therapy """
    SCOPY = 0
    GRAPHY = 1


class Parameters:
    def __init__(self, therapy):
        # selected therapy
        self.therapy = therapy

        # initial health state
        self.initialHealthState = HealthStates.WELL

        # annual treatment cost
        if self.therapy == Therapies.SCOPY:
            self.annualTreatmentCost = Data.Colonoscopy_COST
        else:
            self.annualTreatmentCost = Data.Colonography_COST

        # calculate transition probabilities between states
        prob_matrix_scopy = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX)

        # transition probability matrix of the selected therapy
        self.transRateMatrix = []

        if self.therapy == Therapies.SCOPY:
            # calculate transition rate matrix for the colonoscopy
            self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_scopy)

        elif self.therapy == Therapies.GRAPHY:
            # calculate transition probability matrix for the colonography
            self.transRateMatrix = get_trans_rate_matrix_graphy(
                rate_matrix_scopy=get_trans_rate_matrix(trans_prob_matrix=prob_matrix_scopy),
                graphy_rr=Data.COLONOGRAPHY_RR)

        # annual state costs and utilities
        self.annualStateCosts = Data.ANNUAL_STATE_COST
        self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY

        # discount rate
        self.discountRate = Data.DISCOUNT


def get_trans_prob_matrix(trans_matrix):
    """
    :param trans_matrix: transition matrix containing counts of transitions between states
    :return: transition probability matrix
    """

    # initialize transition probability matrix
    trans_prob_matrix = []

    # for each row in the transition matrix
    for row in trans_matrix:
        # calculate the transition probabilities
        prob_row = np.array(row) / sum(row)
        # add this row of transition probabilities to the transition probability matrix
        trans_prob_matrix.append(prob_row)

    return trans_prob_matrix


def get_trans_rate_matrix(trans_prob_matrix):

    # find the transition rate matrix
    trans_rate_matrix = Markov.discrete_to_continuous(
        trans_prob_matrix=trans_prob_matrix,
        delta_t=1)

    # calculate background mortality rate
    mortality_rate = -np.log(1 - Data.ANNUAL_PROB_BACKGROUND_MORT)

    # add background mortality rate
    for row in trans_rate_matrix:
        row.append(mortality_rate)

    trans_rate_matrix.append([0] * len(HealthStates))
    trans_rate_matrix.append([0] * len(HealthStates))

    return trans_rate_matrix


def get_trans_rate_matrix_graphy(rate_matrix_scopy, graphy_rr):

    # create an empty list of lists
    matrix_graphy = []
    for row in rate_matrix_scopy:
        matrix_graphy.append([0] * len(row))  # adding a row [0, 0, 0, 0, 0]

    # populate the colonography matrix
    # calculate the effect of colonography on non-diagonal elements
    for s in range(len(matrix_graphy)):
        # rates to states
        for next_s in range(s + 1, len(HealthStates) - 1):
            matrix_graphy[s][next_s] = graphy_rr * rate_matrix_scopy[s][next_s]

        # rates of background mortality
        matrix_graphy[s][-1] = rate_matrix_scopy[s][-1]

    return matrix_graphy


# tests
if __name__ == '__main__':
    probMatrix = get_trans_prob_matrix(Data.TRANS_MATRIX)
    rateMatrixScopy = get_trans_rate_matrix(probMatrix)
    rateMatrixGraphy = get_trans_rate_matrix_graphy(rateMatrixScopy, Data.COLONOGRAPHY_RR)

    print(rateMatrixScopy)
    print(rateMatrixGraphy)
