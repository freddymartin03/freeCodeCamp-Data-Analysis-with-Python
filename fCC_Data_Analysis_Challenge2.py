import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education_count = advanced_education.shape[0]
    advanced_education_percent = round(
        ((advanced_education['salary'] == '>50K').sum() / advanced_education_count) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    advanced_education_not = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education_count_not = advanced_education_not.shape[0]
    advanced_education_percent_not = round(
        ((advanced_education_not['salary'] == '>50K').sum() / advanced_education_count_not) * 100, 1)

    # percentage with salary >50K
    higher_education_rich = advanced_education_percent
    lower_education_rich = advanced_education_percent_not

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    country_earning_counts = df[df['salary'] == '>50K']['native-country'].value_counts()

    country_earning_percentages = (country_earning_counts / country_counts) * 100
    country_earning_percentages = country_earning_percentages.round(1)

    highest_earning_country_percentage = country_earning_percentages.max()
    highest_earning_country = country_earning_percentages.idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax())

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
