import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'data/chicago.csv',
              'new york city': 'data/new_york_city.csv',
              'washington': 'data/washington.csv' }
#create a list for months filter
months = ['january','february','march','april','may','june','all']
#create a list for day of the week filter
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    # while loop takes user input and converts it to lowercase strings so we can compare with our list to catch invalid inputs
    while True:
        city = str(input('\nEnter Chicago, New York City or Washington: ')).lower()
        if city in CITY_DATA:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
            #month = str(input('Please enter the month you would like analyze: January, February, March, April, May or June'))
    month = ''
    # while loop takes user input and converts it to lowercase strings so we can compare with our list to catch invalid inputs
    while True:
        month = str(input('\nWhich month you would like analyze: January, February, March, April, May or June or ALL to apply no filter:')).lower()
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            #day = str(input('Would you like to analyze Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?'))
    day = ''
    # while loop takes user input and converts it to lowercase strings so we can compare with our list to catch invalid inputs
    while True:
        day = str(input('\nWould you like to analyze Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday or ALL to apply no filter:')).lower()
        if day in days:
            break

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
    #load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract month from the Start Time column and create a new column
    df['month'] = df['Start Time'].dt.month
    #extrace day of the week from Start Time column and create a new column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #filter by month if applicable
    if month != 'all':
        month = months.index(month) + 1
        #filter by month to create the new DataFrame
        df = df[df['month'] == month]
    #filter by day of the week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]
    month = months[most_common_month - 1]
    print('The most common month is:', month.title())


    # TO DO: display the most common day of week
    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print('The most common day of the week is:', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    count = df['Start Station'].value_counts().max()
    print('Most commonly used start station is: {}, with a count of: {}'.format(common_start_station,count))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    count = df['End Station'].value_counts().max()
    print('Most commonly used end station is: {}, with a count of: {}'.format(common_end_station, count))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station_combo'] = df['Start Station'] + ' & ' + df['End Station']
    #find the station combinations that appeared the most
    common_station_combo = df['Station_combo'].mode()[0]
    #count all the station combinations and find the one with the highest count
    count = df['Station_combo'].value_counts().max()
    print('Most frequent combination of start and end station trip is: {}, with a count of {}'.format(common_station_combo, count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    #convert total travel time to days,hours,minutes, and seconds
    print('The total travel time is:', datetime.timedelta(seconds = total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = int(df['Trip Duration'].mean())
    print('The average travel time is:', datetime.timedelta(seconds = avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print('\nThe count of each gender is:\n', genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yr = int(df['Birth Year'].min())
        recent_yr = int(df['Birth Year'].max())
        common_yr = int(df['Birth Year'].mode()[0])
        #compressed print statement into one
        print('\nThe earliest birth year is: {}. \nThe most recent birth year is: {}. \nThe most common birth year is: {}.'.format(earliest_yr, recent_yr, common_yr))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Function to display 5 rows of raw data upon request by the user and displays the next 5 rows if user answers 'yes' when prompted"""
    #assign dataframe to a local variable
    dataset = df
    #create 'rows' variable to use in indexing and set its value to 0
    rows = 0
    #create a loop to display 5 rows of data at a time if the user enters 'yes'
    while True:
        prompt = str(input('\nWould you like to see 5 rows of the raw data? Enter yes or no.\n')).lower()
        if prompt == 'yes':
            print(dataset.iloc[rows:rows+5,:])
            rows += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
