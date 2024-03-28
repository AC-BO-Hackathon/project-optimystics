
from baybe import Campaign
from baybe.objective import Objective
from baybe.parameters import NumericalDiscreteParameter, SubstanceParameter
from baybe.searchspace import SearchSpace
from baybe.targets import NumericalTarget
from baybe.utils.dataframe import add_fake_results



### Setup

# defining ranges of volumes v_i for each precursor
NUM_PRECURSORS = 6

parameters = [
    NumericalContinuousParameter(
        name=f"v_{k+1}",
        bounds=(0, 60),
    )
    for k in range(NUM_PRECURSORS)
]

# defining the constraint that the sum of all volumes wont exceed 60uL

constraints = [ContinuousLinearEqualityConstraint(
        parameters= [f"v_{k+1}" for k in range(NUM_PRECURSORS)], coefficients=[1.0 for k in range(NUM_PRECURSORS)], rhs=60.0
    )]


searchspace = SearchSpace.from_product(parameters=parameters, constraints=constraints)


### Defining the targets

Target_1 = NumericalTarget(
    name="G1", mode="MATCH", bounds=(900, 1100), transformation="LINEAR"
)
Target_2 = NumericalTarget(
    name="G2", mode="MATCH", bounds=(400, 600), transformation="LINEAR"
)

Target_3 = NumericalTarget(
    name="relaxation_time", mode=TargetMode.MAX,  
)

# Note that the `MATCH` mode seeks to have the target at the mean between the two bounds.
# For example, choosing 95 and 105 will lead the algorithm seeking 100 as the optimal value.
# Thus, using the bounds, it is possible to control both the match target and
# the range around this target that is considered viable.


### Creating the objective

# Now to work with these three targets the objective object must be properly created.
# The mode is set to `DESIRABILITY` and the targets are described in a list.

targets = [Target_1, Target_2, Target_3]

objective = Objective(
    mode="DESIRABILITY",
    targets=targets,
    combine_func="MEAN",
)

### Construct the campaign and run some iterations
campaign = Campaign(
    searchspace=searchspace,
    objective=objective,
)


### Load the existing data

#data = pd.read_csv("./data.csv")
#campaign.add_measurements(data)

### Generation of recommendations
batch_size=96
rec = campaign.recommend(batch_size = batch_size)


### Example with fake data
N_ITERATIONS = 3
for kIter in range(N_ITERATIONS):
    print(f"\n\n#### ITERATION {kIter+1} ####")

    rec = campaign.recommend(batch_size = batch_size)
    print("\nRecommended measurements:\n", rec)

    add_fake_results(rec, campaign)
    print("\nRecommended measurements with fake measured results:\n", rec)

    campaign.add_measurements(rec)

    print("\n\nInternal measurement dataframe computational representation Y:\n")
    print(campaign._measurements_targets_comp)