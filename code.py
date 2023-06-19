import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def organizer(path):

    emp = pd.read_csv(path)

    emp.columns = ["Journée", "Heure", "Module", "Type", "Enseignant", "Salle", "Promotion", "specialité", "Groupe", "Nature"]

    groupes = emp["Groupe"].unique()

    groupes = groupes.tolist()
    groupes.remove("Promo")
    

    groupesEmp = []

    for groupe in groupes:
        df = emp.loc[(emp['Groupe'].str.contains(groupe)) | ((emp['Groupe'] == "Promo") | (emp['Groupe'] == "Sec"))]
        fig, ax =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
        pp = PdfPages(f"groupe{groupe}.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()

    print(groupesEmp)


organizer('Emplois du temps.csv')



