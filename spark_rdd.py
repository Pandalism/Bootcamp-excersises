import re
from datetime import datetime as dt

# We're defining some functions that might be helpful below
# Those will not be evaluated on KATE, but feel free to use them.


def get_words(line):
    return re.compile(r"\w+").findall(line)


def get_hour(rec):
    time_ = dt.utcfromtimestamp(rec["created_at_i"])
    return time_.hour


def extract_time(timestamp):
    return dt.utcfromtimestamp(timestamp)


def get_bucket(rec, min_timestamp, max_timestamp):
    interval = (max_timestamp - min_timestamp + 1) / 200.0
    return int((rec["created_at_i"] - min_timestamp) / interval)

# set function to output 1 if gt 200 otherwise 0
def gt_200(x):
    bool_int = 0
    if x > 200:
        bool_int = 1
    return bool_int


# Beginning of the exercise.


def count_elements_in_dataset(dataset):
    """
    Given a dataset loaded on Spark, return the
    number of elements.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: number of elements in the RDD
    """
    return dataset.count()


def get_first_element(dataset):
    """
    Given a dataset loaded on Spark, return the
    first element

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: the first element of the RDD
    """
    return dataset.first()


def get_all_attributes(dataset):
    """
    Each element is a dictionary of attributes and their values for a post.
    Can you find the set of all attributes used throughout the RDD?
    The function dictionary.keys() gives you the list of attributes of a dictionary.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: all unique attributes collected in a list
    """
    # collect all keys in all elements
    keys = dataset.flatMap(lambda element: element.keys())

    # find the distinct keys
    unique = keys.distinct()

    # return result as list
    return unique.collect()


def get_elements_w_same_attributes(dataset):
    """
    We see that there are more attributes than just the one used in the first element.
    This function should return all elements that have the same attributes
    as the first element.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: an RDD containing only elements with same attributes as the
    first element
    """
    # get first element attributes
    first_keys = list(dataset.first().keys())

    # return filtered RDD
    return dataset.filter(lambda line: first_keys == list(line.keys()))


def get_min_max_timestamps(dataset):
    """
    Find the minimum and maximum timestamp in the dataset

    Hint: the extract_time function defined above can be useful here.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: min and max timestamp in a tuple object
    :rtype: tuple
    """
    # extract timestamps
    timestamps = dataset.map(lambda line: extract_time(line.get('created_at_i')))

    return (timestamps.min(), timestamps.max())


def get_number_of_posts_per_bucket(dataset, min_time, max_time):
    """
    Using the `get_bucket` function defined above, this function should return a
    new RDD that contains the number of elements that fall within each bucket.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :param min_time: Minimum time to consider for buckets (datetime format)
    :param max_time: Maximum time to consider for buckets (datetime format)
    :return: an RDD with number of elements per bucket
    """
    # convert min & max time to 
    epoch = dt.utcfromtimestamp(0)

    def unix_time_millis(dt):
        return int((dt - epoch).total_seconds())

    min_time_i = unix_time_millis(min_time)
    max_time_i = unix_time_millis(max_time)

    # filter through all dataset and find hour and assign as (key,1)
    bucketset = dataset.map(lambda rec: (get_bucket(rec, min_time_i, max_time_i), 1))

    # reduce by key with a moving sum
    output = bucketset.reduceByKey(lambda c1, c2: c1 + c2)

    return output


def get_number_of_posts_per_hour(dataset):
    """
    Using the `get_hour` function defined above, this function should return a
    new RDD that contains the number of elements per hour.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: an RDD with number of elements per hour
    """
    # filter through all dataset and find bucket location and asign as (key,1)
    hourset = dataset.map(lambda rec: (get_hour(rec), 1))

    # reduce by key with a moving sum
    output = hourset.reduceByKey(lambda c1, c2: c1 + c2)

    return output


def get_score_per_hour(dataset):
    """
    The number of points scored by a post is under the attribute `points`.
    Use it to compute the average score received by submissions for each hour.

    Hint: the function get_hour might be useful here.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: an RDD with average score per hour
    """
    # filter through all dataset and find bucket location and asign as (key,(score, 1))
    # wherein key is the hour, score 
    hourset = dataset.map(lambda rec: (get_hour(rec), (rec.get('points'), 1)))

    # reduce by key with a moving sum on both score and count 
    sumset = hourset.reduceByKey(lambda c1, c2: (c1[0] + c2[0], c1[1] + c2[1]))

    # go through sums and find the averages
    output = sumset.map(lambda rec: (rec[0], rec[1][0]/rec[1][1]))
    return output


def get_proportion_of_scores(dataset):
    """
    It may be more useful to look at sucessful posts that get over 200 points.
    Find the proportion of posts that get above 200 points per hour.
    This will be the number of posts with points > 200 divided by the total number of posts at this hour.

    Hint: the function get_hour might be useful here.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: an RDD with the proportion of scores over 200 per hour
    """
    # filter through all dataset and find bucket location and asign as (key,(gt_200(), 1))
    # wherein key is the hour, gt_200(score) is 1 or 0, and 1 is to help count 
    hourset = dataset.map(lambda rec: (get_hour(rec), (gt_200(rec.get('points')), 1)))

    # reduce by key with a moving sum on both score and count 
    sumset = hourset.reduceByKey(lambda c1, c2: (c1[0] + c2[0], c1[1] + c2[1]))

    # go through sums and find the averages
    output = sumset.map(lambda rec: (rec[0], rec[1][0]/rec[1][1]))
    return output


def get_proportion_of_success(dataset):
    """
    Using the `get_words` function defined above to count the
    number of words in the title of each post, look at the proportion
    of successful posts for each title length.

    Note: If an entry in the dataset does not have a title, it should
    be counted as a length of 0.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: an RDD with the proportion of successful post per title length
    """
    # filter through all dataset and title length and asign as (key,(gt_200(), 1))
    # wherein key is the title length, gt_200(score) is 1 or 0, and 1 is to help count 
    titleset = dataset.map(lambda rec: 
        (len(get_words(rec.get('title', ""))),
        (gt_200(rec.get('points')), 1)))

    # reduce by key with a moving sum on both score and count 
    sumset = titleset.reduceByKey(lambda c1, c2: (c1[0] + c2[0], c1[1] + c2[1]))

    # go through sums and find the averages
    output = sumset.map(lambda rec: (rec[0], rec[1][0]/rec[1][1]))
    return output


def get_title_length_distribution(dataset):
    """
    Count for each title length the number of submissions with that length.

    Note: If an entry in the dataset does not have a title, it should
    be counted as a length of 0.

    Hint: the function get_words might be useful here.

    :param dataset: dataset loaded in Spark context
    :type dataset: a Spark RDD
    :return: an RDD with the number of submissions per title length
    """
    # filter through all dataset and title length and asign as (key, 1))
    # wherein key is the title length, and 1 is to help count 
    titleset = dataset.map(lambda rec: 
        (len(get_words(rec.get('title', ""))), 1))

    # reduce by key with a moving sum on count 
    sumset = titleset.reduceByKey(lambda c1, c2: c1 + c2)

    return sumset

