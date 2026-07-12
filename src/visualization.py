import matplotlib.pyplot as plt
import seaborn as sns

def plot_gender_distribution(df):
    colors = ['#A6CEE3', '#B2DF8A']  

    fig, ax = plt.subplots(figsize=(5, 4))

    df["gender"].value_counts().reindex(["Male", "Female"]).plot.pie(
        autopct=lambda p: f'{p:.0f}%',  
        colors=colors,
        startangle=90,
        counterclock=True,
        wedgeprops={'edgecolor': 'white'},
        labels=None, 
        ax=ax
    )

    ax.legend(["Male", "Female"], loc="center left", bbox_to_anchor=(1, 0.5))
    ax.set_title("Gender Distribution")
    ax.set_ylabel("")
    ax.set_aspect('equal') 

    plt.tight_layout()
    plt.savefig("reports/figures/figure1_gender_distribution.png", dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig