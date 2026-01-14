#!/usr/bin/env python
# coding: utf-8

# required package: glob
# install with:
# pip install glob

import json
from glob import glob
import pathlib
import hashlib

hat_files = glob("hats/*.png")

with open("CustomHats.json", encoding="utf-8") as fp:
    hats_file = json.load(fp)

hats = hats_file["hats"]
names = []
for hat in hats:
    names.append(hat["name"])

for hat in hats:
    try:
        assert hat["reshasha"] == hashlib.md5(open("hats/" + hat["resource"],'rb').read()).hexdigest()
        if hat.get("climbresource", None) is not None:
            assert hat["reshashc"] == hashlib.md5(open("hats/" + hat["climbresource"],'rb').read()).hexdigest()
    except:
        print("hat resources missing or changed:", hat)

def find_hat_by_resource(hat_file):
    for hat in hats:
        name = pathlib.Path(hat_file).name
        if hat.get("climbresource") == name or hat.get("resource") == name or hat.get("flipresource") == name or hat.get("backflipresource") == name or hat.get("backresource") == name:
            return hat

new_hat_files = []

for hat_file in hat_files:
    if find_hat_by_resource(hat_file) is None:
        new_hat_files.append(pathlib.Path(hat_file).name)

print("Found new hat files:")
print(new_hat_files)
print("End of new hat files!")

new_hats = dict()
for hat_file in new_hat_files:
    print(hat_file)
    try:
        end_ind = hat_file.index("_")
    except:
        end_ind = hat_file.index(".")
    hat_name = hat_file[:end_ind]
    if hat_name not in new_hats:
        new_hats[hat_name] = []
    new_hats[hat_name].append(hat_file)

hat_packages = []
author = ""

# ask for package name. Will only ask once and assume all hats go into the same package.
new_hats_found = False
if len(list(new_hats.items())) > 0:
    new_hats_found = True
    package_name = input("Enter Package name! (empty for \"Community Hats\"): ")
    if package_name == "":
        package_name = "Community Hats"
else:
    package_name = ""

for hat_name, file_list in new_hats.items():
    hat_dict = dict()
    hat_dict["name"] = hat_name
    hat_dict["package"] = package_name
    hat_dict["condition"] = "None"
    for fn in file_list:
        file_hash = hashlib.md5(open("hats/" + fn,'rb').read()).hexdigest()
        if "adaptive" in fn:
            hat_dict["adaptive"] = True
        if "climb" in fn:
            hat_dict["climbresource"] = fn
            hat_dict["reshashc"] = file_hash
        elif "back" in fn:
            if "flip" in fn:
                hat_dict["flipresource"] = fn
                hat_dict["reshashbf"] = file_hash
            else:
                hat_dict["backresource"] = fn
                hat_dict["reshashb"] = file_hash
        elif "flip" in fn:
            hat_dict["flipresource"] = fn
            hat_dict["reshashf"] = file_hash
        else:
            hat_dict["resource"] = fn
            hat_dict["reshasha"] = file_hash
        if "bounce" in fn:
            hat_dict["bounce"] = True
    if author == "":
        author = input(f"Please input author for {hat_name}: ")
    else: 
        res = input(f"Use {author} as author for {hat_name} [Y/n]: ")
        if res not in "Yy":
            author = input(f"Please input author for {hat_name}: ")
    hat_dict["author"] = author
    hat_packages.append(hat_dict)

for hat_dict in hat_packages:
    if hat_dict not in hats_file["hats"]:
        hats_file["hats"].append(hat_dict)

# Write, but don't overwrite so it can be checked.
if new_hats_found:
    with open('CustomHats_Updated.json', 'w') as fp:
        json.dump(hats_file, fp, indent=4)

