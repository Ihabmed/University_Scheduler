import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import tabula
import os

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def organizer(path):
    tabula.convert_into(path, "output.csv", output_format="csv", pages='all')
    # emp.columns = ["Journée", "Heure", "Module", "Type", 
    # "Enseignant", "Salle", "Promotion", "Spésialité", "Groupe", "Nature"]
    emp = pd.read_csv("output.csv")
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
    if not os.path.isdir(path.split(".")[0]):
        pwd = os.getcwd()
        dirpath = os.path.join(pwd, path.split(".")[0])
        os.mkdir(dirpath)

    for groupe in grp:
        df = emp.loc[(emp['Groupe'].isin(groupe))]
        fig, ax =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
        pp = PdfPages(f"/home/ihab/Downloads/groupe{groupe[0]}.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()

    os.remove('output.csv')



organizer('/home/ihab/Downloads/L3.pdf')





# speciality = emp["Spésialité"].unique()
# speciality = speciality.tolist()
# spec = []
# for i in range(len(speciality)):
#     if "+" in speciality[i]:
#         continue
#     spec1 = []
#     spec1.append(speciality[i])
#     for j in range(len(speciality)):
#         if ((speciality[i] + "+") in speciality[j]) or (("+" + speciality[i]) in speciality[j]):
#             spec1.append(speciality[j])
#     spec.append(spec1)

# for s in spec:
#     df = emp.loc[emp["Spésialité"].isin(s)]
#     print(df)