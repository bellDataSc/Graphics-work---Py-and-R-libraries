
    chart_img = Image.open(chart_path)
    final_height = chart_img.height + img_table.height + 30
    combined_img = Image.new("RGB", (chart_img.width, final_height), (255, 255, 255))
    combined_img.paste(chart_img, (0, 0))
    combined_img.paste(img_table, (0, chart_img.height + 30))

    final_path = f"/content/Ordering_Family_{family_name}.png"
    combined_img.save(final_path)
    print(f"Final chart saved at: {final_path}")
