import tkinter
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib
import tabula
import os
from tkinter import *

# emp.columns = ["Journée", "Heure", "Module", "Type", 
    # "Enseignant", "Salle", "Promotion", "Spésialité", "Groupe", "Nature"]
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def group_orginizer(dest, emp):
    groupes = emp["Groupe"].unique()
    groupes = groupes.tolist()
    for i in range(len(groupes)):
        if type(groupes[i]) != str:
            groupes.remove(groupes[i])
    grp = []
    for i in range(len(groupes)):
        if "+" in groupes[i] or not has_numbers(groupes[i]):
            continue
        tmp = []
        tmp.append(groupes[i])
        for j in range(len(groupes)):
            if ((groupes[i] + "+") in groupes[j]) or (("+" + groupes[i]) in groupes[j]) or (not has_numbers(groupes[j])):
                tmp.append(groupes[j])
        grp.append(tmp)

    for groupe in grp:
        df = emp.loc[(emp['Groupe'].isin(groupe))]
        fig, ax = plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
        pp = PdfPages(f"{dest}/groupe{groupe[0]}.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()

def organizer(path, dest):
    tabula.convert_into(path, os.path.dirname(path) + "/" + "output.csv", output_format="csv", pages='all')
    emp = pd.read_csv(os.path.dirname(path) + "/" + "output.csv")
    emp = emp.drop(columns=['Promotion'])
    emp = emp.drop(columns=['Nature'])
    speciality = emp["Spésialité"].unique()
    speciality = speciality.tolist()
    tabs = []
    if len(speciality) > 1:
        spec = []
        for i in range(len(speciality)):
            if "+" in speciality[i]:
                continue
            spec1 = []
            spec1.append(speciality[i])
            for j in range(len(speciality)):
                if ((speciality[i] + "+") in speciality[j]) or (("+" + speciality[i]) in speciality[j]):
                    spec1.append(speciality[j])
            spec.append(spec1)
        for s in spec:
            df = emp.loc[emp["Spésialité"].isin(s)]
            p = os.path.join(dest, s[0])
            tabs.append(p)
            if not os.path.exists(p):
                os.mkdir(p)
            else:
                for dir in os.listdir(p):
                    os.remove(p + "/" + dir)
            df.to_csv(f"{p}/output1.csv", sep=",",index=False, encoding='utf-8')
            group_orginizer(p, pd.read_csv(f"{p}/output1.csv"))
            os.remove(f"{p}/output1.csv")
    else:
        p = dest + "/" + os.path.basename(path).split(".")[0]
        tabs.append(p)
        if os.path.exists(p):
            for dir in os.listdir(p):
                os.remove(p + "/" + dir)
            os.rmdir(p)
        os.mkdir(p)
        emp = emp.drop(columns=['Spésialité'])
        group_orginizer(p, emp)
    os.remove(os.path.dirname(path) + "/" + "output.csv")
    return tabs
