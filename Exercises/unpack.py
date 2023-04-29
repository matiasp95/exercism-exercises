"""Functions which helps the locomotive engineer to keep track of the train."""
import unittest

def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
   
    return list(args)

#input_data = [(1,5,2,7,4), (1,5), (1,), (1,9,3), (1,10,6,3,9,8,4,14,24,7)]
#print(get_list_of_wagons(*input_data))

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a, b, c, *rest = each_wagons_id

    *x,  = c, *missing_wagons, *rest,a,b
    return x

input_data = [([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]),
             ([3, 27, 1, 14, 10, 4, 12, 6, 23, 17, 13, 22, 28, 19], [8, 10, 5, 9, 36, 7, 20]),
             ([4, 2, 1], [8, 6, 15]), 
             ([3, 14, 1, 25, 7, 19, 10], [8, 6, 4, 5, 9, 21, 2, 13])
             ]
output_data = [[1, 3, 17, 6, 15, 7, 4,  12, 6, 3, 13, 2, 5],
                [1, 8, 10, 5, 9, 36, 7, 20, 14, 10, 4, 12, 6, 23, 17, 13, 22, 28, 19, 3, 27], 
                [1, 8, 6, 15, 4, 2], 
                [1, 8, 6, 4, 5, 9, 21, 2, 13, 25, 7, 19, 10, 3, 14]
            ]

#print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    #Other option: return {**route, **more_route_information}

    route["stops"] = list(kwargs.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}

#print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # Easier:  return list(map(list, zip(*wagons_rows)))
    [[a,b,c],[d,e,f],[g,h,i]] = wagons_rows
    return [[a,d,g],[b,e,h],[c,f,i]]

    

print(fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ]))
