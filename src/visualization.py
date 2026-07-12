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

def plot_scores_distribution(df):
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.histplot(
        data=df, 
        x="wellbeing_score", 
        bins=15,                   
        kde=True,                 
        color="#2b5c8f",         
        alpha=0.4,                 
        edgecolor="white",         
        line_kws={"linewidth": 2.5, "color": "#1d3f66"} 
    )

    plt.xlabel("Mental Well-being Score", fontsize=11, labelpad=8)
    plt.ylabel("Frequency", fontsize=11, labelpad=8)
    plt.title("Distribution of Mental Well-being Scores", fontsize=12, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig("reports/figures/wellbeing_distribution.png", dpi=300, bbox_inches="tight")
    plt.show()
    
    return None

def plot_correlation_boxplot(df):
    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 5))
    sns.regplot(
        data=df,
        x="hours",
        y="wellbeing_score",
        scatter_kws={"s": 70, "alpha": 0.65, "edgecolor": "white", "linewidths": 0.5}, 
        line_kws={"linewidth": 2.5, "color": "#1f77b4"},                             
        ci=95                                                                        
    )

    plt.xlabel("Hours Spent on Social Media", fontsize=11, labelpad=8)
    plt.ylabel("Mental Well-being Score", fontsize=11, labelpad=8)
    plt.title("Relationship Between Social Media Usage and Mental Well-being", fontsize=12, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig("reports/figures/relationship_scatter_plot.png", dpi=300, bbox_inches="tight")
    plt.show()
    
    return None

def correlation_matrix(df):
    plt.figure(figsize=(8, 5))
    corr = df.corr()
    sns.heatmap(
        corr, 
        annot=True, 
        fmt=".2f", 
        cmap="coolwarm", 
        cbar=True, 
        square=True, 
        linewidths=0.5, 
        linecolor='white'
    )
    plt.savefig("reports/figures/correlation_matrix.png", dpi=300, bbox_inches="tight")
    plt.title("Correlation Matrix of Key Survey Variables", fontsize=12, pad=18, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    return None


def plot_wellbeing_gender_boxplot(df):
    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 5))
    custom_palette = {"Male": "#5dade2", "Female": "#ec7063"} 