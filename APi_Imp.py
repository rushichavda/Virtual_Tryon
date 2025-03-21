
# from gradio_client import Client, handle_file
# from gradio_client import Client, file

# client = Client("franciszzj/Leffa")

# result = client.predict(
#   src_image_path=handle_file("C:\GoDream\Virtual_Tryon\person image\handsome-young-cheerful-man.jpg"),
#   ref_image_path=handle_file('C:\GoDream\Virtual_Tryon\clothes image\images (2).jpeg'),
#   vt_garment_type="upper_body",
#   api_name="/leffa_predict_vt"
# )

# print(result)

import os
import shutil
from gradio_client import Client, handle_file

client = Client("franciszzj/Leffa")


person_dir = r"C:\GoDream\Virtual_Tryon\person image"
clothes_dir = r"C:\GoDream\Virtual_Tryon\clothes image"
output_dir = r"C:\GoDream\Virtual_Tryon\output"

os.makedirs(output_dir, exist_ok=True)

person_images = [f for f in os.listdir(person_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
clothes_images = [f for f in os.listdir(clothes_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

for person_image in person_images:
    for clothes_image in clothes_images:
        person_path = os.path.join(person_dir, person_image)
        clothes_path = os.path.join(clothes_dir, clothes_image)

        print(f"Processing: {person_image} with {clothes_image}")

        try:
            result = client.predict(
                src_image_path=handle_file(person_path),
                ref_image_path=handle_file(clothes_path),
                vt_garment_type="upper_body",
                api_name="/leffa_predict_vt"
            )

            
            generated_image_path = result[0] if isinstance(result, tuple) and len(result) > 0 else None

            output_filename = f"{os.path.splitext(person_image)[0]}_{os.path.splitext(clothes_image)[0]}.webp"
            output_path = os.path.join(output_dir, output_filename)

            
            if generated_image_path and os.path.exists(generated_image_path):
                shutil.move(generated_image_path, output_path)
                print(f"✅ Saved: {output_path}")
            else:
                print(f"⚠️ Unexpected API response: {result}")

        except Exception as e:
            print(f"❌ Error processing {person_image} with {clothes_image}: {e}")

print("🎉 All combinations processed! Results saved in the output folder.")
