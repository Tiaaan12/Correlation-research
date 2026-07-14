from data_cleaning import load_data, clean_data, encode_data
from statistics import descriptive_statistics, correlation_analysis, linear_regression
from visualization import plot_gender_distribution, plot_social_mediahours_distribution, plot_scores_distribution, plot_correlation_boxplot, plot_correlation_matrix, plot_wellbeing_gender_boxplot, plot_averagescore_line_graph, plot_frequency_distribution, plot_age_distribution 

def main():

    df = load_data("data/raw/survey_data.csv")
    df = clean_data(df)
    df = encode_data(df)

    descriptive_statistics(df)
    correlation_analysis(df)
    linear_regression(df)

    plot_gender_distribution(df)
    plot_social_mediahours_distribution(df)
    plot_scores_distribution(df)
    plot_correlation_boxplot(df)
    plot_correlation_matrix(df)
    plot_wellbeing_gender_boxplot(df)
    plot_averagescore_line_graph(df)
    plot_frequency_distribution(df)
    plot_age_distribution(df)

if __name__ == "__main__":
    main()