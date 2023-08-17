library(healthyR.data)
library(healthyR)
library(ggplot2)
library(dplyr)
library(forcats)
library(purrr)

df <- healthyR_data |>
  filter(payer_grouping != '?') |>
  category_counts_tbl(
    .count_col = payer_grouping
    , .arrange = TRUE
    , ip_op_flag
  ) |>
  group_by(ip_op_flag) |>
  mutate(order_var = sprintf("%02i", as.integer(rank(n))))

  
ggplot(df, aes(x = order_var, y = n)) +
  geom_col() +
  facet_wrap(~ ip_op_flag, scale = "free", drop = TRUE) +
  scale_x_discrete(labels =  with(df, as.character(payer_grouping) |> 
                                    set_names(order_var))) +
  xlab(NULL) +
  theme(axis.text.x = element_text(angle = 90, hjust=1, vjust=.5)) +
  coord_flip() +
  theme_minimal()