import InputData as D
import ParameterClasses as P
import MarkovModelClasses as Cls
import Support as Support


# simulating colonoscopy screening
# create a cohort
cohort_scopy = Cls.Cohort(id=0,
                          pop_size=D.POP_SIZE,
                          parameters=P.Parameters(therapy=P.Therapies.SCOPY))
# simulate the cohort
cohort_scopy.simulate(sim_length=D.SIM_LENGTH)

# simulating colonography screening
# create a cohort
cohort_graphy = Cls.Cohort(id=1,
                           pop_size=D.POP_SIZE,
                           parameters=P.Parameters(therapy=P.Therapies.GRAPHY))
# simulate the cohort
cohort_graphy.simulate(sim_length=D.SIM_LENGTH)

# print the estimates for the mean survival time and mean time to cancer
Support.print_outcomes(sim_outcomes=cohort_scopy.cohortOutcomes,
                       therapy_name=P.Therapies.SCOPY)
Support.print_outcomes(sim_outcomes=cohort_graphy.cohortOutcomes,
                       therapy_name=P.Therapies.GRAPHY)

# draw survival curves and histograms
Support.plot_survival_curves_and_histograms(sim_outcomes_scopy=cohort_scopy.cohortOutcomes,
                                            sim_outcomes_graphy=cohort_graphy.cohortOutcomes)


# print comparative outcomes
Support.print_comparative_outcomes(sim_outcomes_scopy=cohort_scopy.cohortOutcomes,
                                   sim_outcomes_graphy=cohort_graphy.cohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(sim_outcomes_scopy=cohort_scopy.cohortOutcomes,
                       sim_outcomes_graphy=cohort_graphy.cohortOutcomes)
