import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import re


def organizer(path):

    emp = pd.read_csv(path)

    emp.columns = ["Journée", "Heure", "Module", "Type", "Enseignant", "Salle", "Promotion", "specialité", "Groupe", "Nature"]

    groupes = emp["Groupe"].unique()

    groupes = groupes.tolist()
    
    regex = re.compile(r"[a-zA-Z]+")

    for groupe in groupes:
        if(regex.match(groupe)):
            groupes.remove(groupe)
    print(groupes)

    for groupe in groupes:
        df = emp.loc[(emp['Groupe'].str.contains(groupe)) | (emp['Groupe'] == "Promo") | (emp['Groupe'] == "Sec") | (emp['Groupe'] == "sec")]
        fig, ax =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
        pp = PdfPages(f"groupe{groupe}.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()



organizer('Emp1erS2.csv')



