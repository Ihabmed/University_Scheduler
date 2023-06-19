import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import re
import tabula
from functools import reduce
import os


def organizer(path):

    tabula.convert_into(path, "output.csv", output_format="csv", pages='all')

    # emp.columns = ["Journée", "Heure", "Module", "Type", "Enseignant", "Salle", "Promotion", "specialité", "Groupe", "Nature"]
    emp = pd.read_csv("output.csv")

    groupes = emp["Groupe"].unique()

    groupes = groupes.tolist()
    
    regex = re.compile(r"[a-zA-Z]+")

    groupes = list(filter(lambda e: len(e)==1, groupes))

    pwd = os.getcwd()

    dirpath = os.path.join(pwd, path.split(".")[0])

    os.mkdir(dirpath)
    

    for groupe in groupes:
        df = emp.loc[(emp['Groupe'].str.contains(groupe)) | (emp['Groupe'] == "Promo") | (emp['Groupe'] == "Sec") | (emp['Groupe'] == "sec")]
        fig, ax =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
        pp = PdfPages(f"{path.split('.')[0]}/groupe{groupe}.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()



organizer('math.pdf')





