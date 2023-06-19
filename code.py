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

    for i in range(len(groupes)):
        df = emp.loc[(emp['Groupe'] == str(i+1)) | (emp['Groupe'] == "Promo")]
        fig, ax =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
        pp = PdfPages(f"groupe{i+1}.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()

    print(groupesEmp)


organizer('Emplois du temps.csv')


