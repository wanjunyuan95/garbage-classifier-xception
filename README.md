# Webapp for garbage classification using Deep Neural Network

## Background

While recycling may seem as simple as throwing our waste to a bin and waiting for it to be send to a plant to perform it's magical processes, it may not be the case most of the times. As according to the United States'Environmental Protection Agency (EPA) seems to agree that the estimated 75% of American waste is recyclable but only 30% of it is actually recycled[1]. Moreover, according to CBC, contamination is the technical name for non-recyclable material or garbage in the recycling system, from leftover food in containers to non-recyclable plastic packaging to more obvious garbage such as clothing and propane tanks. For example, major cities such as Toronto have a contamination rate as high as 25%, which essentially turns recycling materials into unrecyclable waste[2].

One of the issues with recycling that may be solve with AI-driven model is the issue of improper sorting. Consumers may struggle to determine the composition of waste goods due to the multitude of waste-material types and varying rules, and so incorrectly designate an item as recyclable or non-recyclable. Mixing recyclable and non-recyclable goods lowers the value of to-be-recycled materials and makes it more difficult to sell them, as well as increasing the volume of recyclables that end up in landfills. As a result, one potential AI application is the use of picture classification to identify and assist consumers in recognising the material composition of their trash items and, as a result, their recyclability.

I have created a Xception model in the one of the files then in order to create an app to show case my model, I have decided to use Streamlit. To explain it briefly, Streamlit specialise in Machine Learning and Data science function where we can build apps in a Python environment with a simple API. It also integrates well with various Python packages such as Tensorflow, Pandas, Pytorch and Keras.


## Functionality

The app I have built will be localhosted meaning it will not be deploy for now but will definitely do it once it has become more refined. Inside the app, we are only accepting jpg and png format of photos and then classify it into one of the 12 classes (paper, cardboard, plastic, metal, trash, battery, shoe, clothes, green glass, brown glass, white glass and biological waste). Moreover, I am also pre-processing the images before feeding it into the model itself. It will reshape the photos as according to the original model. It will then output a table where it shows the probability of each classified classes and select the highest one as our final results.
