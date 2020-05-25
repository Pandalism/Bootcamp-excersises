# Part 2: GROUP BY


def freq_risk_per_violation():
    """
    Find out the distribution of the risk exposure of all the violations reported in the database
    The first column of the result should 'risk_category' and the second column the count.
    :return: a string representing the SQL query
    :rtype: str
    """
    return "SELECT risk_category, count(*) FROM violations GROUP BY risk_category"


def freq_risk_per_violation_water():
    """
    Find out the distribution of the risk exposure of all the violations reported in the database
    that are *water related*. Sort them by frequency from high to low.
    :return: a string representing the SQL query
    :rtype: str
    """
    return "SELECT risk_category, count(*) FROM violations WHERE description LIKE '%water%' GROUP BY risk_category ORDER BY count(*) DESC"


def frequency_of_inspections_types():
    """
    What types of inspections does the authorities conduct and how often do they occur in general.
    Calculate the distribution of different types of inspections with their frequency (type, frequency)
    based on inspections records. Sort them in ascending order based on frequency.
    :return: a string representing the SQL query
    :rtype: str
    """
    return "SELECT type, count(type) FROM inspections GROUP BY type ORDER BY count(type)"


def avg_score_by_inspection_type():
    """
    What is the average score given to restaurants based on the type of inspection?
    Based on the results, identify the types of inspections that are not scored (NULL)
    and remove those categories from the resultset. The 'average_score' should be rounded
    to one decimal. Sort the results in ascending order based on the average score.
    Hint: use the function ROUND(score, 1)
    :return: a string representing the SQL query
    :rtype: str
    """
    return "SELECT type,ROUND((SUM(score) / COUNT(score) ),1) FROM inspections WHERE SCORE IS NOT NULL GROUP BY type ORDER BY (SUM(score) / COUNT(score))


def owner_per_restaurant_count():
    """
    Find the restaurant owners (owner_name) that own one or multiple restaurants in the city
    with the number of restaurants (num_restaurants) they own.
    Find the first top 10 owners ordered by descending order using the number of restaurants.
    :return: a string representing the SQL query
    :rtype: str
    """
    return "SELECT owner_name, count(owner_name) FROM businesses GROUP BY owner_name ORDER BY count(owner_name) DESC LIMIT 10"
