from gradio_client import Client, handle_file

# Initialize client for the API
client = Client("franciszzj/Leffa")

# Paths or URLs of images
source_image = "path/to/person_image.jpg"  # Replace with local path or URL
garment_image = "path/to/garment_image.jpg"  # Replace with local path or URL

# Call API for virtual try-on
result = client.predict(
    src_image_path=handle_file(source_image),   # Person wearing clothes
    ref_image_path=handle_file(garment_image),  # Garment to try on
    ref_acceleration="false",  # Keep "false" unless you need faster but lower-quality results
    step=30,   # Inference steps (higher = better quality, but slower)
    scale=2.5,  # Guidance scale (adjust for image quality)
    seed=42,  # Random seed (change for different results)
    vt_model_type="viton_hd",  # Model type: 'viton_hd' (default) or 'dress_code'
    vt_garment_type="upper_body",  # Garment type: 'upper_body', 'lower_body', 'dresses'
    vt_repaint="false",  # Repaint mode (set to "true" if necessary)
    api_name="/leffa_predict_vt"
)

# Extract the generated virtual try-on image
generated_image_url = result[0]["url"]
print(f"Generated Virtual Try-On Image: {generated_image_url}")
