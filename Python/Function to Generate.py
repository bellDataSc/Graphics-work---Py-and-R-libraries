def generate_family_chart(data_history_file, code_file, family_name):
    
    df_codes = pd.read_excel(code_file)
    df_codes.columns = ["Code", "Family"]

    
    family_items = df_codes.loc[df_codes["Family"] == family_name, "Code"].tolist()
    if len(family_items) == 0:
        print(f"No items found for the family '{family_name}'")
        return

 
    df = pd.read_excel(data_history_file)
    df = df[df["ITEM"].isin(family_items)]
    df = df[df["UF"].isin(state_order)]

    
    last_value_col = [c for c in df.columns if isinstance(c, str) and "-" in c][-1]
    df_plot = df[["ITEM", "UF", last_value_col]].copy()
    df_plot.rename(columns={last_value_col: "Value"}, inplace=True)

    fig, ax = plt.subplots(figsize=(16, 7))
    fig.subplots_adjust(bottom=0.35, top=0.85)

    for i, item in enumerate(df_plot["ITEM"].unique()):
        df_item = df_plot[df_plot["ITEM"] == item]
        df_item = df_item.set_index("UF").reindex(state_order)
        ax.plot(df_item.index, df_item["Value"], label=item,
                color=family_colors[i % len(family_colors)],
                linewidth=2.5, marker="o", markersize=6)

    
    ax.set_ylabel("Price (R$/m³)", fontsize=11)
    ax.set_xlabel("")
    ax.grid(True, linestyle="--", alpha=0.6)

    
    ax.set_title("Graph 46 – Ordering of the Washed Sand Family",
                 fontsize=14, fontweight="bold", color="#1F4E79", pad=20, loc="center")
    ax.text(0.5, 1.02,
            "Input prices by family, across states and regions (R$/m³)",
            transform=ax.transAxes, fontsize=10, color="gray", ha="center")

    
    y_text = ax.get_ylim()[0] - (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.08
    offset = 0
    for region, states in regions.items():
        mid = offset + (len(states) - 1) / 2
        ax.text(mid, y_text, region, ha="center", va="center",
                fontsize=10, fontweight="bold", color="black")
        offset += len(states)

    
    ax.legend().remove()

    chart_path = f"/content/Chart_Family_{family_name}.png"
    plt.savefig(chart_path, bbox_inches="tight", dpi=300)
    plt.close()
