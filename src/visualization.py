import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import pandas as pd

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
    
    sns.boxplot(
    data=df,
    x="gender",
    y="wellbeing_score",
    hue="gender",                        
    palette=custom_palette,
    legend=False,                    
    width=0.4,                       
    linewidth=1.5,                      
    fliersize=4,                         
    boxprops=dict(alpha=0.5)           
    )
    
    sns.stripplot(
        data=df,
        x="gender",
        y="wellbeing_score",
        color="#2c3e50",                    
        alpha=0.35,                         
        jitter=0.12                        
    )
    
    plt.xlabel("Gender", fontsize=11, labelpad=8)
    plt.ylabel("Mental Well-being Score", fontsize=11, labelpad=8)
    plt.title("Distribution of Mental Well-being Scores by Gender", fontsize=12, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig("reports/figures/wellbeing_by_gender.png", dpi=300, bbox_inches="tight")
    plt.show()
    
    return None

def plot_averagescore_line_graph(df):         

    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 5))
    avg_scores = df.groupby("hours")["wellbeing_score"].mean()
    
    plt.plot(
    avg_scores.index, 
    avg_scores.values, 
    color="#2b5c8f",         
    linewidth=2.5,           
    marker='o',                 
    markersize=8,             
    markerfacecolor='white',  
    markeredgewidth=2           
    )
    
    plt.xlabel("Hours Spent on Social Media", fontsize=11, labelpad=8)
    plt.ylabel("Average Well-being Score", fontsize=11, labelpad=8)
    plt.title("Average Mental Well-being Score per Social Media Usage Hour", fontsize=12, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig("reports/figures/average_wellbeing_line_graph.png", dpi=300, bbox_inches="tight")
    plt.show()


def plot_frequency_distribution(df):
    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 5))
    platforms = []
    for p in df["platforms"]:
        split_platforms = str(p).split(";")
        platforms.extend([item.strip() for item in split_platforms if item.strip()])

    platform_count = Counter(platforms)
    platform_df = pd.DataFrame(
        list(platform_count.items()), 
        columns=["Platform", "Count"]
    ).sort_values(by="Count", ascending=True)

    plt.barh(
    platform_df["Platform"], 
    platform_df["Count"], 
    color="#2b5c8f",          
    alpha=0.75,               
    edgecolor="white",       
    height=0.6                
    )

    plt.xlabel("Number of Respondents (Frequency)", fontsize=11, labelpad=8)
    plt.ylabel("Social Media Platforms", fontsize=11, labelpad=8)
    plt.title("Frequency Distribution of Active Social Media Platform Engagement", fontsize=12, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig("reports/figures/appendix_platform_frequency.png", dpi=300, bbox_inches='tight')
    plt.show()

    return None
