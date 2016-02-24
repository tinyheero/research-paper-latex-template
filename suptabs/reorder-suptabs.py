#!/usr/bin/env python
# Generate Order of Supplemental Tables

import os
import shutil
import pandas as pd

sup_tabs_directory = os.path.realpath(os.path.dirname(__file__))
main_directory = os.path.realpath(os.path.join(sup_tabs_directory, os.pardir))

results_latex = os.path.join(main_directory, "results.tex")
methods_latex = os.path.join(main_directory, "methods.tex")
supmethods_latex = os.path.join(main_directory, "supmethods.tex")
discussion_latex = os.path.join(main_directory, "discussion.tex")

catalog_filename = os.path.join(sup_tabs_directory, "catalog.tsv")
order_filename = os.path.join(sup_tabs_directory, "order.tsv")

catalog = pd.read_csv(catalog_filename, sep="\t")

text = ""
with open(results_latex) as f:
    text += f.read()
with open(methods_latex) as f:
    text += f.read()
with open(supmethods_latex) as f:
    text += f.read()
with open(discussion_latex) as f:
    text += f.read()

for idx, label in catalog["latex_label"].iteritems():
    try:
        catalog.loc[idx, "location"] = text.index(label)
    except ValueError:
        raise Exception("label " + label + " not found")

catalog.sort_values("location", inplace=True)
catalog["order"] = range(len(catalog.index))
catalog.sort_values("latex_label", inplace=True)

catalog[["latex_label", "order"]].to_csv(order_filename, sep="\t", index=False)
