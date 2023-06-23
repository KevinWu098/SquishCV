from DeepImageSearch import Load_Data, Search_Setup
import gradio as gr

image_list = Load_Data().from_folder(['Squishmallow_Images'])

st = Search_Setup(image_list=image_list, model_name='vgg19', pretrained=True)
st.run_index()

def imageSearch(image):
    similarImages = st.get_similar_images(image_path=image, number_of_images=1)
    return list(similarImages.values())

title = "Find Your Squishmallow 🧸"
description = "This Space demos an image similarity system built for finding Squishmallows that represent you!"

gr.Interface(
    imageSearch,
    inputs=gr.Image(type="filepath"),
    outputs=gr.Gallery(columns=1, object_fit="contain"),
    title=title,
    description=description,
).launch()