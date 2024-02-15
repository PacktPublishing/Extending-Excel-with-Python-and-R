# Lib Load
library(healthyR.ai)
library(dplyr)

glimpse(head(df, 2))

# Pass data through pre-processor
rec_obj <- hai_xgboost_data_prepper(
  .data = df, 
  .recipe_formula = price ~ .
)
rec_obj

# Now see the juiced output
get_juiced_data(rec_obj) |>
  head(2) |>
  glimpse()

# Now perform modeling using the hai_auto_xgboost() function
auto_xgb <- hai_auto_xgboost(
  .data = df,
  .rec_obj = rec_obj,
  .best_metric = "rsq",
  .num_cores = 10,
  .model_type = "regression"
)

xgb_wflw_fit <- auto_xgb$model_info$fitted_wflw
class(xgb_wflw_fit)
mod_spec <- xgb_wflw_fit[["fit"]][["actions"]][["model"]][["spec"]]
mod_spec

# Save the model
save_path <- paste0(getwd(), "/Chapter14/")
saveRDS(xgb_wflw_fit, paste0(save_path, "xgb_wflw_fit.rds"))
        