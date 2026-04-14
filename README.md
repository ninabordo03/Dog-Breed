In this project, I used convolutional neural networks to determine a dog's breed based on its image.

The model was made in Google Colab, whereas the deployment was made in Python using Streamlit.

The first thing to do was to load the data from kaggle, then load labels csv for labels that contain image ID and breed.

After that, I checked the breed count and then did one-hot encoding on labels data prediction column.

Then, I loaded the images, converted them to an array and normalized them, then I checked the shape and size of x and y data.

Afterwards, I built the model network architecture and then I split the data and fit it into the model and create an accuracy plot.
