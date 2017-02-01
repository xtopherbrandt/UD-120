#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    # Create list of (age, net_worth, error) for all data
    cleaned_data = map( lambda p, f, t: (f[0], t[0], abs(p[0]-t[0])), predictions, ages, net_worths )

    # Sort by Error
    cleaned_data.sort( key=getKey )

    # Remove 9 highest errors

    
    return cleaned_data[0:81]

def getKey (item):
    return item[2]