"""

    MADE BY ALEXIS SANCHEZ IG4 - BU-CROCCS

"""

"""Function to calculate how much box2 is overlapped by box1
    
    Parameters
    ----------
    box1 : Object
    box2 : Object
        
    Returns
    -------
    float
        the percentage of overlapping of box2 by box1
"""


def intersection(box1, box2):
    x_overlap = max(0, min(box1.x_max, box2.x_max) - max(box1.x_min, box2.x_min))
    y_overlap = max(0, min(box1.y_max, box2.y_max) - max(box1.y_min, box2.y_min))
    intersec = (x_overlap * y_overlap)/box2.get_area()
    return intersec

#box1 = personne
#box2 = helmet

#def is_in(box1, box2):
   # return (box2.x_min >= box1.x_min and box2.y_min >= box1.y_min and box1.x_max >= box2.x_max and ((box1.y_max - box1.y_min)*0.3+box1.y_min) >= box2.y_max)


"""To know if the person in parameter is the driver of the motorbike

    Parameters
    ----------
    person : Object
        Object predicted as 'person'
    motorcycle : Object
        Object predicted as 'motorbike'
        
    Returns
    -------
    bool
        true if the person is the driver of the motorbike
        
"""


def is_driver(motorcycle, person):
    driver = False
    intersect = intersection(motorcycle, person)
    if intersect >= 0.4:
        driver = True

    return driver


"""To know if the person in parameter wears the helmet

    Parameters
    ----------
    person : Object
        Object predicted as 'person'
    helmet : Object
        Object predicted as 'helmet'

    Returns
    -------
    bool
        true if the person wears the helmet
"""


def wear_helmet(person, helmet):
    return intersection(person, helmet) >= 0.95
