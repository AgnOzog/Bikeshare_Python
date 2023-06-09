import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

weekday_list = ['all', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday' 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input(
            "\n Which city would you like to analyse? (Chicago, New york city, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid city name")

   # city = check_user_input(
    #    'Would you like to see the data for chicago, new york city or washington?\n', 'c')
    while True:
        months = ['January', 'February', 'March',
                  'April', 'June', 'May', 'all']
        month = input(
            "\n If you would like to filter your data by month, chose from january to june, otherwise enter 'all'\n").title()
        if month in months:
            break
        else:
            print("\n Please enter a valid month")

    # month = check_user_input(
    #    "If you would like to filter your data by month name from january to june, provide the name of the month otherwise enter 'all'\n", 'm')
    while True:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday', 'None']
        day = input("\n To filter data by specific day placese enter day of the week that you are interested in (monday - sunday), otherwise enter 'all'\n").title()
        if day in days:
            break
        else:
            print("\n Please enter a valid day")

    # day = check_user_input(
    #    "To filter data by specific day placese enter day of the week that you are interested in (monday - sunday), otherwise enter 'all'\n", 'd')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name()

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march',
                  'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is :", most_common_month)
    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is :", most_common_day_of_week)
    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is :", most_common_start_station)
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is :", most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[[
        'Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"
          .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_counts = df['Gender'].value_counts()
        print("\nThe counts of each gender are:\n", gender_counts)
        # Display counts of user types
        print("Users Types in Data are:", df['User Types'].value_counts())
        # Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        print("\nThe oldest user is born of the year", earliest)
        most_recent = int(df['Birth Year'].max())
        print("The youngest user is born of the year", most_recent)
        common = int(df['Birth Year'].mode()[0])
        print("Most users are born of the year", common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    while True:
        response = ['yes', 'no']
        choice = input(
            "Would you like to view individual trip data (5 entries)? Type 'yes' or 'no'\n").lower()
        if choice in response:
            if choice == 'yes':
                start = 0
                end = 5
                data = df.iloc[start:end, :9]
                print(data)
            break
        else:
            print("Please enter a valid response")
    if choice == 'yes':
        while True:
            choice_2 = input(
                "Would you like to view more trip data? Type 'yes' or 'no'\n").lower()
            if choice_2 in response:
                if choice_2 == 'yes':
                    start += 5
                    end += 5
                    data = df.iloc[start:end, :9]
                    print(data)
                else:
                    break
            else:
                print("Please enter a valid response")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
