import math


def distance(coord1, coord2):
    """
    Calculate the Haversine distance between two coordinates.

    Parameters:
    - coord1: Tuple, representing (latitude, longitude) of the first point.
    - coord2: Tuple, representing (latitude, longitude) of the second point.

    Returns:
    - Distance in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Extracting latitude and longitude values
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Converting latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance
