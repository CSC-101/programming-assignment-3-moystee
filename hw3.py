import data
import county_demographics
import build_data
import hw3_tests
#Task 1
# Purpose: Sum up the '2014 Population' from each CountyDemographics object
def population_total(county_list: list) -> int:
    total_population = sum(county.population['2014 Population'] for county in county_list)
    return total_population
#Task 2
#Purpose: Return a list of county demographics objects from the input list that are within the specified state
def filter_by_state(county_list: list, state_abbreviation: str) -> list:
    filtered_counties = [county for county in county_list if county.state == state_abbreviation]
    return filtered_counties
#Task 3
#Purpose: Return the total 2014 sub-population across the set of counties in the provided list for the specified key of interest
def population_by_education(county_list: list, education_key: str) -> float:
    total_population = 0
    for county in county_list:
        if education_key in county.education:
            percent = county.education[education_key]
            total_population += (percent / 100) * county.population['2014 Population']
    return total_population
#Purpose: Return the total 2014 sub-population across the set of counties in the provided list for the specified key of interest
def population_by_ethnicity(county_list: list, ethnicity_key: str) -> float:
    total_population = 0
    for county in county_list:
        if ethnicity_key in county.ethnicities:
            total_population += county.ethnicities[ethnicity_key]
    return total_population
#Purpose: Return the total 2014 sub-population indicated by income key 'Persons Below Poverty Level' across the set of
# counties in the provided list for the specified key of interest.
def population_below_poverty_level(county_list: list, income_key: str) -> float:
    total_below_income_level = 0
    for county in county_list:
        if income_key in county.income:
            total_below_income_level += county.income[income_key]
    return total_below_income_level
#Task 4
#Purpose: return the specified 2014 sub-population as a percentage of the total 2014 population across the set of
# counties in the provided list for the specified key of interest
def percent_by_education(county_list: list, education_key: str) -> float:
    total_population = population_total(county_list)
    total_education_population = 0
    for county in county_list:
        if education_key in county.education:
            total_education_population += county.education[education_key]
    if total_population == 0:
        return 0
    return (total_education_population / total_population) * 100
#Purpose: return the specified 2014 sub-population as a percentage of the total 2014 population across the set of
# counties in the provided list for the specified key of interest.
def percent_by_ethnicity(county_list: list, ethnicity_key: str) -> float:
    total_population = population_total(county_list)
    total_ethnicity_population = 0
    for county in county_list:
        if ethnicity_key in county.ethnicity:
            total_ethnicity_population += county.ethnicity[ethnicity_key]
    if total_population == 0:
        return 0
    return (total_ethnicity_population / total_population) * 100
#Purpose: return the 2014 sub-population indicated by income key 'Persons Below Poverty Level' as a percentage of the
# total 2014 population across the set of counties in the provided list for the specified key of interest.
def percent_below_poverty_level(county_list: list, income_key: str) -> float:
    total_population = population_total(county_list)
    total_poverty_population = 0
    for county in county_list:
        if income_key in county.income:
            total_poverty_population += county.income[income_key]
    if total_population == 0:
        return 0
    return (total_poverty_population / total_population) * 100
#Task 5:
#Purpose: eturn a list of all county demographics objects for which the value for the specified key is greater than or
# less than (as appropriate by function name) the specified threshold value
def education_greater_than(county_list: list, education_key: str, threshold: str) -> list:
    counties_above_threshold = []
    for county in county_list:
        if education_key in county.education:
            if county.education[education_key] > threshold:
                counties_above_threshold.append(county)
    return counties_above_threshold
def education_less_than(county_list: list, education_key: str, threshold: str) -> list:
    counties_below_threshold = []
    for county in county_list:
        if education_key in county.education:
            if county.education[education_key] < threshold:
                counties_below_threshold.append(county)
    return counties_below_threshold
#Purpose: return a list of all county demographics objects for which the value for the specified key is greater than or
# less than (as appropriate by function name) the specified threshold value
def ethnicity_greater_than(county_list: list, ethnicity_key: str, threshold: str) -> list:
    counties_above_threshold = []
    for county in county_list:
        if ethnicity_key in county.ethnicities:
            if county.ethnicities[ethnicity_key] > threshold:
                counties_above_threshold.append(county)
    return counties_above_threshold
def ethnicity_less_than(county_list: list, ethnicity_key: str, threshold: str) -> list:
    counties_below_threshold = []
    for county in county_list:
        if ethnicity_key in county.ethnicities:
            if county.ethnicities[ethnicity_key] < threshold:
                counties_below_threshold.append(county)
    return counties_below_threshold
#Purpose: return a list of all county demographics objects for which the value for key 'Persons Below Poverty Level' is
# greater than or less than (as appropriate by function name) the specified threshold value
def below_poverty_level_greater_than(county_list: list, income_key: str, threshold: str) -> list:
    counties_above_threshold = []
    for county in county_list:
        if income_key in county.income:
            if county.income[income_key] > threshold:
                counties_above_threshold.append(county)
    return counties_above_threshold
def below_poverty_level_less_than(county_list: list, income_key: str, threshold: str) -> list:
    counties_below_threshold = []
    for county in county_list:
        if income_key in county.income:
            if county.income[income_key] < threshold:
                counties_below_threshold.append(county)
    return counties_below_threshold