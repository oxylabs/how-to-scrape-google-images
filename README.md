# How To Scrape Google Images

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

- [Free Google Images Scraper](#free-google-images-scraper)
    + [Prerequisites](#prerequisites)
    + [Installation](#installation)
    + [Getting an image to query](#getting-an-image-to-query)
    + [Scraping Google Images](#scraping-google-images)
    + [Notes](#notes)
- [Scrape public Google Images data with Oxylabs API](#scrape-public-google-images-data-with-oxylabs-api)
    + [Step 1 - Setting up the environment](#step-1---setting-up-the-environment)
    + [Step 2- Import the required libraries](#step-2--import-the-required-libraries)
    + [Step 3 - Structure the payload](#step-3---structure-the-payload)
    + [Step 4 - Make the request](#step-4---make-the-request)
    + [Step 5 - Extract the data and save it in a CSV file](#step-5---extract-the-data-and-save-it-in-a-csv-file)

## Free Google Images Scraper

A free tool used to get Google Images search results based on a provided image URL.

### Prerequisites

To run this tool, you need to have Python 3.11 installed in your system.

### Installation

Open up a terminal window, navigate to this repository and run this command:

```make install```

### Getting an image to query

First of all, find an image you want to query Google Images with.

For this example, we'll be using an image of a cat from the Wikipedia page on cats.

Make sure to copy the direct image address, like this:

<img width="437" alt="image" src="https://github.com/oxylabs/how-to-scrape-google-images/assets/44357929/6c086183-3bc2-4a37-ab47-ff797eb8b88c">

The retrieved URL must end in `.jpg`, `.png`, or any other image format. Here's the URL of the copied image:

https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Kittyply_edit1.jpg/440px-Kittyply_edit1.jpg

Save the URL you copied, it will be used for scraping Google Images results based on that image.

### Scraping Google Images

To get results from Google Images based on an image URL, simply run this command in your terminal:

```make scrape URL="<your_image_url>"```

With the image URL we retrieved earlier, the command would look like this:

```make scrape URL="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Kittyply_edit1.jpg/440px-Kittyply_edit1.jpg"```

Make sure to surround the URL with quotation marks, otherwise the tool might have trouble parsing it.

After running the command, your terminal should look something like this:

<img width="1160" alt="image" src="https://github.com/oxylabs/how-to-scrape-google-images/assets/44357929/5c7ff49a-c8a7-4728-915a-34e90ee2e1f0">


After the tool has finished running, you should notice that an `images.csv` file appeared in your current directory.

This data in this file has these columns for the Google Images results for your provided image:

- `title` - The title of the page the image was found on.
- `image_url` - The static Google Images URL for that image.
- `source_url` - The source URL of the page the image found on.

Here's an example of how the data can look like:

<img width="1479" alt="image" src="https://github.com/oxylabs/how-to-scrape-google-images/assets/44357929/1a11048c-746d-4770-bfac-78eb4c9dbf69">

### Notes

In case the code doesn't work or your project is of bigger scale, please refer to the second part of the tutorial. There, we showcase how to scrape public data with Oxylabs Scraper API.

## Scrape public Google Images data with Oxylabs API 

You can also scrape public Google Images data with [Google Images Search API](https://oxylabs.io/products/scraper-api/serp/google/images). Keep in mind that this is a paid tool but you may get a free 7-day trial. Once you get the trial (or a subscription), you'll have to create a user account on the Oxylabs dashboard and get the API credentials. These credentials will be used in the later stages.

### Step 1 - Setting up the environment

To get started, we must have Python 3.6+ installed and running on your system. Also, we need the following packages to put our code into action:

- requests - for sending HTTP requests to Oxylabs API.

- Pandas - for saving our output data in dataframes and saving in CSV files.

To install these packages, we can use the following command:

```pip install requests pandas ```

Running this command will install all the required packages.

### Step 2- Import the required libraries

After the installation of packages, start by creating a new Python file and import the required libraries using the following code:

```import requests```
```import pandas as pd```

### Step 3 - Structure the payload

The Oxylabs Image Scraper API has some parameters that can be set to structure the payload and make the request accordingly. The details of these parameters can be found in the official [documentation](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/google/images?_gl=1*1kgcw2x*_gcl_aw*R0NMLjE3MDk4MjEyOTguQ2p3S0NBaUE2S1d2QmhBUkVpd0FGUFpNN25wc2s1OWgtcW9lRWlzX0I4aDVvVWlMeGdtaUtxSk9BNDY5Nm9rbkhhVEYxSGV1WHdZTXRob0NWZVVRQXZEX0J3RQ..*_gcl_au*MTY0ODg5MzY2Ni4xNzEzNzY4NDc1LjU2NzE3MzM0My4xNzE1MjU3NTEwLjE3MTUyNTc1MDk.) by Oxylabs.

The payload is structured as follows:

```
payload = {
"source": "google_images",
   "domain": "com",
   "query": "<search_image_URL>",
   "context": [
       {
           "key": "search_operators",
           "value": [
               {"key": "site", "value": "example.com"},
               {"key": "filetype", "value": "html"},
               {"key": "inurl", "value": "image"},
           ],
       }
   ],
   "parse": "true",
   "geo_location": "United States"


}
```
NOTE: Make sure to replace the ```query``` parameter value with the required search image URL.

The ```context``` parameter is used to apply some search filters. For example, our search operators force the API to scrape only the links from Google image search results that belong to ```example.com```. If you remove this site key from the ```search_operators```, the Image Scraper API may return related results from all the websites.

The search operators ```filetype:``` html and ```inurl:image``` define search criteria to only retrieve results with a file type of HTML and where "image" is included in the URL.

The ```parse``` parameter is set to true to get the results parsed in the JSON format. Additionally, you can add pages and ```start_page``` parameters to the payload to scrape multiple result pages starting from the ```start_page```. A value of 1 is the default value for both the parameters.

### Step 4 - Make the request

After creating the payload structure, you can initiate a POST request to Oxylabs’ API using the following code segment.

```
response = requests.request(
   "POST",
   "https://realtime.oxylabs.io/v1/queries",
   auth=(USERNAME, PASSWORD),
   json=payload,
)
```

NOTE: Make sure to replace ```username``` and ```password``` with your API credentials. The response received can be viewed in the JSON format.

### Step 5 - Extract the data and save it in a CSV file

Now, we can extract the required images from the response object. The response object has a key ```results``` that contains all the related image data. We will extract and save all the image data in the data frame. Later, this dataframe can be saved in a CSV file using the following code.

```result = response.json()["results"][0]["content"]
image_results = result["results"]["organic"]

# Create a DataFrame
df = pd.DataFrame(columns=["Image Title", "Image Description", "Image URL"])

for i in image_results:
   title = i["title"]
   description = i["desc"]
   url = i["url"]

   df = pd.concat(
       [pd.DataFrame([[title, description, url]], columns=df.columns), df],
       ignore_index=True,
   )

# Copy the data to CSV and JSON files
df.to_csv("google_image_results.csv", index=False)
df.to_json("google_image_results.json", orient="split", index=False)
```
Now, let's take an [example URL](https://upload.wikimedia.org/wikipedia/commons/a/a3/June_odd-eyed-cat.jpg) of a cat as the query image and put all the code together to make more cognitive sense. Assume that we want to scrape the first page from Google Images and want to restrict search to [wikipedia.org](http://wikipedia.org/) only.  Here is what the code looks like:

```
# Import Required libraries
import requests
import pandas as pd
from pprint import pprint

# Set your Oxylabs API credentials
USERNAME = "<your_username>"
PASSWORD = "<your_password>"

# Structure payload.
payload = {
   "source": "google_images",
   "domain": "com",
   "query": "https://upload.wikimedia.org/wikipedia/commons/a/a3/June_odd-eyed-cat.jpg",
   "context": [
       {
           "key": "search_operators",
           "value": [
               {"key": "site", "value": "wikipedia.org"},
               {"key": "filetype", "value": "html"},
               {"key": "inurl", "value": "image"},
           ],
       }
   ],
   "parse": "true",
   "geo_location": "United States"

}

# Get response.
response = requests.request(
   "POST",
   "https://realtime.oxylabs.io/v1/queries",
   auth=(USERNAME, PASSWORD),
   json=payload,
)

# Extract data from the response
result = response.json()["results"][0]["content"]
image_results = result["results"]["organic"]

# Create a DataFrame
df = pd.DataFrame(columns=["Image Title", "Image Description", "Image URL"])

for i in image_results:
   title = i["title"]
   description = i["desc"]
   url = i["url"]

   df = pd.concat(
       [pd.DataFrame([[title, description, url]], columns=df.columns), df],
       ignore_index=True,
   )

   # Print the data on the screen
   print("Image Name: " + title)
   print("Image Description: " + description)
   print("Image URL: " + url)

# Copy the data to CSV and JSON files
df.to_csv("google_image_results.csv", index=False)
df.to_json("google_image_results.json", orient="split", index=False)
```
Here is what our output looks like:

<img width="812" alt="image" src="https://github.com/oxylabs/how-to-scrape-google-images/assets/103110131/62ffaeeb-197d-40e4-93bd-3d7d6c9103f3">

The complete API response for this API request can be found [here](https://pastebin.com/sKJF12g9).

Looking to scrape data from other Google sources? [Google Sheets for Basic Web Scraping](https://github.com/oxylabs/web-scraping-google-sheets), [How to Scrape Google Shopping Results](https://github.com/oxylabs/scrape-google-shopping), [Google Play Scraper](https://github.com/oxylabs/google-play-scraper), [How To Scrape Google Jobs](https://github.com/oxylabs/how-to-scrape-google-jobs), [Google News Scrpaer](https://github.com/oxylabs/google-news-scraper), [How to Scrape Google Scholar](https://github.com/oxylabs/how-to-scrape-google-scholar), [How to Scrape Google Flights with Python](https://github.com/oxylabs/how-to-scrape-google-flights),  [Scrape Google Search Results](https://github.com/oxylabs/scrape-google-python), [Scrape Google Trends](https://github.com/oxylabs/how-to-scrape-google-trends)
