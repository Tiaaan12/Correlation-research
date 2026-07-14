from scipy.stats import linregress
import pandas as pd

def descriptive_statistics(df):
    df = df.describe()
    df['hours'].describe()

    df["age_group"] = pd.cut(
    df["age"],
    bins=[17,19,21,23],
    labels=["18-19","20-21","22-23"]
    )
    
    return df

def correlation_analysis(df):
    r = df['hours'].corr(df['wellbeing_score'])
    print(f"Correlation coefficient (r): {r}")
    
def linear_regression(df):
    output = linregress(df['hours'], df['wellbeing_score'])
    
    lregression_output = pd.DataFrame({
        "Parameter" : ["Slope", "Intercept", "R-value", "P-value", "Standard Error"],
        "Value" : [output.slope, output.intercept, output.rvalue, output.pvalue, output.stderr]
        
    })

    print(lregression_output)
    return lregression_output
