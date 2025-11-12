generate_family_chart <- function(data_history_file, code_file, family_name) {

  df_codes <- read_excel(code_file, col_names = c("Code", "Family"))
  family_items <- df_codes %>% filter(Family == family_name) %>% pull(Code)
  
  if (length(family_items) == 0) {
    message(paste("No items found for family:", family_name))
    return(NULL)
  }

  df <- read_excel(data_history_file)
  df <- df %>% filter(ITEM %in% family_items, UF %in% state_order)


  last_col <- tail(grep("-", names(df), value = TRUE), 1)
  
  df_plot <- df %>%
    select(ITEM, UF, all_of(last_col)) %>%
    rename(Value = all_of(last_col))

  p <- ggplot(df_plot, aes(x = factor(UF, levels = state_order), y = Value, group = ITEM)) +
    geom_line(aes(color = ITEM), size = 1.2) +
    geom_point(aes(color = ITEM), size = 2.5) +
    scale_color_manual(values = family_colors) +
    labs(
      title = "Graph 46 – Ordering of the Washed Sand Family",
      subtitle = "Input prices by family, across states and regions (R$/m³)",
      y = "Price (R$/m³)", x = NULL
    ) +
    theme_minimal(base_size = 12) +
    theme(
      plot.title = element_text(size = 14, face = "bold", color = "#1F4E79", hjust = 0.5),
      plot.subtitle = element_text(size = 10, color = "gray40", hjust = 0.5),
      axis.text.x = element_text(angle = 0, vjust = 1),
      legend.position = "none",
      panel.grid.minor = element_blank()
    )


  region_labels <- data.frame(
    UF = unlist(regions),
    region = rep(names(regions), times = sapply(regions, length))
  )
  
  p <- p + geom_text(
    data = region_labels %>%
      group_by(region) %>%
      summarize(UF = UF[ceiling(length(UF)/2)]),
    aes(x = UF, y = min(df_plot$Value) * 0.9, label = region),
    size = 3.2, fontface = "bold"
  )
  
  ggsave(filename = paste0("/content/Chart_Family_", family_name, ".png"),
         plot = p, width = 14, height = 6, dpi = 300)







  
