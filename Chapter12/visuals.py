import pandas as pd
from plotnine import ggplot, aes, geom_bin2d, facet_wrap, theme_minimal, labs, scale_fill_manual, geom_boxplot, geom_point, geom_line, geom_smooth, scale_color_manual, geom_histogram

# Define the file path
file_path = "./Chapter12/diamonds.xlsx"

# Load the dataset into a pandas DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Define a colorblind-friendly color palette
color_palette = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]

# Plot using plotnine
(
    ggplot(df, aes(x='carat', y='price', fill='cut')) +
    geom_bin2d(bins=20) +  # Adjust the bins parameter as needed
    facet_wrap('~ clarity', scales='free') +
    theme_minimal() +
    labs(
        x='Carat',
        y='Price',
        title='Diamonds Data',
        fill='Cut'
    ) +
    scale_fill_manual(values=color_palette)
)

# Plot using plotnine
(
    ggplot(df, aes(x='carat', y='price', fill='cut')) +
    geom_boxplot(alpha=1/5, outlier_color="lightgrey") +
    facet_wrap('~ clarity', scales='free') +
    theme_minimal() +
    labs(
        x='Carat',
        y='Price',
        title='Diamonds Data',
        fill='Cut'
    ) +
    scale_fill_manual(values=color_palette)
)

# Plot the mean price by clarity and cut
(
    ggplot(df.groupby(['clarity', 'cut']).mean().reset_index(), aes(x='clarity', y='price', group='cut', color='cut')) +
    geom_point() +
    geom_line() +
    geom_smooth() +
    facet_wrap('~ cut', ncol=2) +
    labs(
        x='Clarity',
        y='Mean Price',
        title='Mean Price by Clarity and Cut',
        color='Cut'
    ) +
    theme_minimal() +
    scale_color_manual(values=color_palette)
)


# Calculate mean price per carat by clarity, color, and cut
df_mean = df.groupby(['cut', 'color', 'clarity']).apply(lambda x: (x['price'] / x['carat']).mean()).reset_index(name='m')

# Plot mean price per carat by clarity, color, and cut
(
    ggplot(df_mean, aes(x='color', y='m', group='clarity', color='clarity')) +
    geom_point() +
    geom_line() +
    facet_wrap('~ cut', ncol=2, scales='free') +
    labs(
        x='Clarity',
        y='Mean Price',
        title='Mean Price per Carat by Clarity, Color and Cut',
        color='Cut'
    ) +
    scale_color_manual(values=color_palette)
)

# Create a histogram of price by Cut
(
    ggplot(df, aes(x='price')) +
    geom_histogram(fill='lightblue', color='black') +
    theme_minimal() +
    facet_wrap('~ cut', ncol=2, scales='free') +
    labs(x='Price', y='Frequency', title='Price Histogram by Cut')
)
