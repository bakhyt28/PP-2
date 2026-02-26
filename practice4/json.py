import json

FILE_NAME = "sample-data.json"   # name of the JSON file

# open JSON file and load data
with open(FILE_NAME, "r", encoding="utf-8") as file:
    json_data = json.load(file)

# get list of interface data
interfaces = json_data.get("imdata", [])

# print table header
print("Interface Status")
print("=" * 75)
print(f"{'DN':55} {'Speed':8} {'MTU':6}")
print("-" * 75)

# go through each element in the list
for element in interfaces:

    # skip element if it is not a valid dictionary
    if not isinstance(element, dict) or len(element) == 0:
        continue

    # get object name and object data
    key_name = next(iter(element))
    object_data = element.get(key_name, {})

    # extract attributes dictionary
    attributes = object_data.get("attributes", {})

    # get needed values from attributes
    dn_value = attributes.get("dn", "")
    speed_value = attributes.get("speed", "")
    mtu_value = attributes.get("mtu", "")

    # print formatted table row
    print(f"{dn_value:55} {speed_value:8} {mtu_value:6}")