summary_data <- df_plot %>%
    group_by(ITEM) %>%
    summarize(
      Leader = mean(Value, na.rm = TRUE),
      Minimum = min(Value, na.rm = TRUE),
      Maximum = max(Value, na.rm = TRUE),
      Amplitude = ifelse(Minimum == 0, 0, (Maximum - Minimum) / Minimum * 100)
    ) %>%
    mutate(
      Description = paste(family_name, "- m³"),
      Color = family_colors[1:n()]
    )



table_plot <- gridExtra::tableGrob(
    summary_data %>%
      select(ITEM, Description, Leader, Minimum, Maximum, Amplitude),
    rows = NULL,
    theme = gridExtra::ttheme_default(
      core = list(fg_params = list(cex = 0.8)),
      colhead = list(fg_params = list(cex = 0.8, fontface = "bold"))
    )
  )


