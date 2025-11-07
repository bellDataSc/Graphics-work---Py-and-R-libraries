
    summary_data = []
    for i, item in enumerate(df_plot["ITEM"].unique()):
        values = df_plot[df_plot["ITEM"] == item]["Value"]
        avg = values.mean()
        min_v = values.min()
        max_v = values.max()
        amplitude = (max_v - min_v) / min_v * 100 if min_v != 0 else 0
        summary_data.append({
            "color": family_colors[i],
            "item": item,
            "Description": f"{family_name} - m³",
            "Leader": f"R$ {avg:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "Minimum": f"R$ {min_v:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "Maximum": f"R$ {max_v:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "Amplitude": f"{amplitude:.0f}%"
        })

    width = 1600
    height = 200 + 40 * len(summary_data)
    img_table = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img_table)
    font = ImageFont.load_default()

    headers = ["", "ITEM", "DESCRIPTION AND UNIT", "LEADER", "MINIMUM", "MAXIMUM", "AMPLITUDE"]
    x_positions = [40, 120, 350, 850, 1000, 1150, 1300]

    
    y = 25
    for x, h in zip(x_positions, headers):
        draw.text((x, y), h, fill=(0, 0, 0), font=font)
    y += 25
    draw.line((40, y, 1500, y), fill=(0, 0, 0))

    
    for idx, row in enumerate(summary_data):
        y += 25
        bg_color = (240, 240, 240) if idx % 2 == 0 else (255, 255, 255)
        draw.rectangle((30, y - 5, 1550, y + 25), fill=bg_color, outline=(220, 220, 220))
        draw.rectangle((45, y + 2, 65, y + 17), fill=row["color"])
        draw.text((120, y), row["item"], fill=(0, 0, 0), font=font)
        draw.text((350, y), row["Description"], fill=(0, 0, 0), font=font)
        draw.text((850, y), row["Leader"], fill=(0, 0, 0), font=font)
        draw.text((1000, y), row["Minimum"], fill=(0, 0, 0), font=font)
        draw.text((1150, y), row["Maximum"], fill=(0, 0, 0), font=font)
        draw.text((1300, y), row["Amplitude"], fill=(0, 0, 0), font=font)

    table_path = f"/content/Table_Family_{family_name}.png"
    img_table.save(table_path)
