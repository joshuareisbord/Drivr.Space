from csv_navigator import get_specific_model, get_all_models_by_make, get_tags_and_index_from_master_list
import json


def generate_research_response_json(make: str, model: str) -> json:
    """
    This will compile the information on the vehicle in question, and return it as JSON
    :param make: vehicle make
    :param model: vehicle model
    :return: json containing information about all models of the specific vehicle in question
    """

    # Get all the vehicles and populate each with respective data
    index_keys = get_tags_and_index_from_master_list()
    results = get_specific_model(model, get_all_models_by_make(make), exact_model=True)

    if len(results["models"]) != 0:
        results = results["models"]
        entries = []
        for vehicle in results:
            thisVehicle = [{"make": vehicle[index_keys["make"]],
                          "model": vehicle[index_keys["model"]],
                          "year": vehicle[index_keys["year"]],
                          "vehicle_class": vehicle[index_keys["VClass"]],
                          "mpg": vehicle[index_keys["comb08"]],
                          "fuel_grade": vehicle[index_keys["fuelType"]],
                          "drive": vehicle[index_keys["drive"]],
                          "transmission": vehicle[index_keys["trany"]],
                          "cylinders": vehicle[index_keys["cylinders"]],
                          "displacement": vehicle[index_keys["displ"]]}]
            entries.append(thisVehicle)

    else:
        return {"entries": None}

    return {"entries": entries}


if __name__ == '__main__':
    print(generate_research_response_json("Volkswagen", "CC"))


