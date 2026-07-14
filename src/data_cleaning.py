import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    df = df.shape
    df = df.dropna() 
    df = df.drop_duplicates() 
    return df

def encode_data(df):
    df.columns = [
        "gender",
        "age",
        "platforms",
        "hours",
        "q1",
        "q2",
        "q3",
        "q4",
        "q5"
    ]
    
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    legend_mapping = {
        "Strongly Disagree": 1,
        "Disagree": 2,
        "Neutral": 3,
        "Agree": 4,
        "Strongly Agree": 5
    }
    
    for col in ["q1", "q2", "q3", "q4", "q5"]:
        df[col] = df[col].map(legend_mapping)

    print(df.isnull().sum())
    
    df['wellbeing_score'] = df[['q1', 'q2', 'q3', 'q4', 'q5']].sum(axis=1)
    
    df.to_csv("data/processed/Encoded Dataset.csv", index=False)

    return df
