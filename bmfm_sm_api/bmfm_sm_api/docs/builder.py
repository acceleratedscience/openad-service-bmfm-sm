import json
import os
from typing import Optional

def doc_builder(documentation_source, properties_supported=[]):
    """designed to build documentation for BMFMSM defived Examples
    e.g
    Property: <cmd>TRAINSET_CYP2D6</cmd>
    - Description: TRAINSET_CYP2D6
    - return type: float
    - Return value range: 0 to 1

    -Example: <cmd>get molecule property TRAINSET_CYP2D6 for CC(C)CC1=CC=C(C=C1)C(C)C(=O)O</cmd>

                result: 0

    """
    help = []

    smiles = []
    properties_all = False
    if properties_supported == []:
        properties_all = True
    else:
        properties_all = False
    for prop in documentation_source["properties"]:
        # Cater for when no examples provided
        if properties_all is False and prop["display_name"] not in properties_supported:
            continue
        # If No example provided mark as NA
        if prop["example"] == "":
            example = "N/A"
        else:
            example_return = prop["example"].split(",")[1].split(" ")
            if len(example_return) > 1:  # If example or / result is a range of results
                example_return = f"[ {','.join(example_return)} ] "
            else:
                example_return = example_return[0]
            example = f"""<cmd>get molecule property {prop['param_id']} for {prop['example'].split(',')[0]}</cmd>
            result: {example_return}"""
            if prop["example"].split(",")[0] not in smiles:
                smiles.append(prop["example"].split(",")[0])
            help_element = f"""Property: <cmd>{prop['param_id']}</cmd>
    - Description: {prop['display_name']} 
    - return type: {prop['type']}
    - Return value range: {prop['min_value'].split(',')[0]} to {prop['max_value'].split(',')[0]} 
    -Example of command generating property {prop['param_id']}:    {example}
         """
        help.append({"name": prop["display_name"], "description": help_element})
    return help

def doc_generate(json_file_path: Optional[str]=None):
    if not json_file_path:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the JSON file
        json_file_path = os.path.join(current_dir, 'BMFMSM.json')
    with open(json_file_path, "r") as file:
        help = json.load(file)
        return doc_builder(help, [])

if __name__ == "__main__":
    with open("bmfm_sm_api/docs/BMFMSM.json", "r") as file:
        help = json.load(file)
        for x in doc_builder(help, []):
            print(x)
