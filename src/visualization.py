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

def plot_social_mediahours_distribution(df):
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df, 
        x="hours", 
        bins=10, 
        kde=True,                  
        color="#3498db",          
        alpha=0.4,                 
        edgecolor="white",         
        line_kws={"linewidth": 2}  
    )

    plt.xlabel("Hours Spent", fontsize=11, fontweight='regular', labelpad=8)
    plt.ylabel("Frequency", fontsize=11, fontweight='regular', labelpad=8)
    plt.title("Distribution of Social Media Usage Hours", fontsize=12, pad=15)
    plt.tight_layout()
    plt.savefig("reports/figures/social_media_distribution.png", dpi=300, bbox_inches="tight")
    plt.show()
    
    return None
    
    