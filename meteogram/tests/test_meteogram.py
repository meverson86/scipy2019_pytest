"""Test use of the meteogram module."""

from meteogram import meteogram
import datetime
from numpy.testing import assert_almost_equal

#
# Example starter test
#


def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify
    assert result == freezing_degC

    # Cleanup - none necessary


#
# Instructor led introductory examples
#
def test_title_case():

    # Setup
    in_string = "this is a test string"
    desired = "This Is A Test String"

    # Exercise
    actual = in_string.title()

    # Verify
    assert actual == desired

    # Clean up - none necessary


#
# Instructor led examples of numerical comparison
#

#
# Exercise 1
#
def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.
    """
    # Setup
    start = datetime.datetime(2018, 1, 5, 1)
    end = datetime.datetime(2018, 1, 9, 1)
    station = "FSD"

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    truth_url = "https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=05&hour1=01&minute1=00&year2=2018&month2=01&day2=09&hour2=01&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes"
    assert result_url == truth_url


def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    # Setup
    start = datetime.datetime(2018, 10, 11, 11)
    end = datetime.datetime(2018, 10, 16, 11)
    station = "FSD"

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    truth_url = "https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2018&month1=10&day1=11&hour1=11&minute1=00&year2=2018&month2=10&day2=16&hour2=11&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes"
    assert result_url == truth_url


#
# Exercise 1 - Stop Here
#
def test_does_three_equal_three():
    assert 3 == 3


def test_floating_subtraction():
    # Setup
    desired = 0.293

    # Exercise
    actual = 1 - 0.707

    # Verify
    # assert abs(actual - desired) < 0.000001
    # import the assert from numpy
    assert_almost_equal(actual, desired)

    # Cleanup - none


#
# Exercise 2 - Add calculation tests here
#
def test_wind_components_north():

    speed = 10
    direction = 0

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = 0
    true_v = -10

    assert_almost_equal(u, true_u)
    assert_almost_equal(v, true_v)


def test_wind_components_northeast():

    speed = 10
    direction = 45

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = -7.0710
    true_v = -7.0710

    assert_almost_equal(u, true_u, 4)
    assert_almost_equal(v, true_v, 4)


#

# Exercise 2 - Stop Here
#

#
# Instructor led mock example
#

#
# Exercise 3
#

#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
