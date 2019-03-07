# myanimelist classifier
Little project to create a multi-label anime classifier to predict age, hair colour and gender from character pictures scraped from myanimelist. 

The classifier used was a convolutional neural network made using the fastai library.

## Running the scraper
The scraper downloads the web page html of given anime page off myanimelist and searches through the a tags to obtain the character images. 

Sadly the pictures need to be classified by hand :(, so send me an email and I can send you the zip of the images I classified.

## Preprocessing images
To match the format of the pre-trained weights from Imagenet the character images are padded to square and scaled down to 224px. 

To run the preprocessing place character images in directory and set path in padder.py and resizer.py 

