# Dog Breed
This is a Convolutional Neural Network project to determine the breed of a dog based on its image.
First, I loaded the data from kaggle and loaded labels csv for labels that contain image ID and breed.
Then, I checked the breed count and did one-hot encoding on labels data prediction column.
After that, I loaded the images, converted them to an array and normalized them.
Then I checked the shape and size of x and y data, built the model network architecture, split the data and fit it into the model and create an accuracy plot.
After all, I saved the model as "dog_breed.h5" and deployed it using the Streamlit library on Python and called it "app.py".
