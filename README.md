# How To Scrape Google Images

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/how-to-scrape-google-scholar/refs/heads/main/Google-Scraper-API-1090x275.png)](https://oxylabs.io/products/scraper-api/serp/google?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=how-to-scrape-google-images-github&transaction_id=102c8d36f7f0d0e5797b8f26152160)

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
### Notes
Different from the Free Google Image scraper, this particular scraper scrapes based on query, rather than the image URL. Get more information about this approach on our blog post on [How to Scrape Google Lens Results](https://oxylabs.io/blog/how-to-scrape-google-lens-results). 

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

The Google Image Scraper API has the ```source```, ```query```, and ```context``` parameters that are mandatory if you want to extract Google Images. All other parameters, such as ```geo_location```, ```parse```, and ```pages```, are optional and allow you to modify the result according to your needs. The details of these and other parameters can be found in the official [documentation](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/targets/google/search/image-search). 

The payload is structured as follows:

```python
# Request payload with API parameters
payload = {
    "source": "google_search",
    "query": "cute cat",
    "geo_location": "United States", # Localize results for US
    "context": [
        {"key": "tbm", "value": "isch"}, # Scrapes only Google Images
    ],
    "parse": True, # Automatically parse HTML into JSON
    "pages": 2 # Scrape as many pages as needed
}

```
NOTE: Make sure to replace the ```query``` parameter value with the search term for which you want to find relevant images.

You may also use the Advanced Google Search Operators to filter results. For example, to find images that are only present on Unsplash, modify your ```query``` parameter value to ```cute cats inurl: unsplash```.

The ```parse``` parameter is set to ```True``` to automatically parse the results and receive them in structured JSON format. 

Additionally, you can retireve your results in Markdown format by setting `markdown` parameter to `true`. This will give your and easy-to-read output for various workflows and AI tools.

Furthermore, you can use ```pages``` and ```start_page``` parameters to scrape multiple result pages starting from the ```start_page```. A value of ```1``` is the default value for both the parameters.

### Step 4 - Make the request

After creating the payload structure, you can initiate a POST request to Oxylabs’ API using the following code segment.

```python
# Use your Oxylabs Web Scraper API credentials
USERNAME = "your_API_username"
PASSWORD = "your_API_password"

# Send a request to Oxylabs Web Scraper API
response = requests.post(
   "https://realtime.oxylabs.io/v1/queries",
   auth=(USERNAME, PASSWORD),
   json=payload
)

# Print the response
print(response.json())
```

NOTE: Make sure to replace ```username``` and ```password``` with your API credentials. The response received can be viewed in the JSON format.

### Step 5 - Extract the data and save it in a CSV file

Now, we can extract the required images from the response object. The response object has a key ```results``` that contains all the related image data. We will extract and save all the image data in the data frame. Later, this dataframe can be saved in a CSV file using the following code.

```python
# Get the response data
response_data = response.json()

all_images = []
# Loop through each page in the results
for page in response_data["results"]:
    # Get the organic results from each page
    organic_results = page["content"]["results"]["organic"]
    # Extract image data from each organic result
    for image in organic_results:
        all_images.append({
            "title": image.get("title", ""),
            "link": image.get("link", ""),
            "image": image.get("image", ""),
            "domain": image.get("domain", ""),
            "position": image.get("pos", ""),
            "position_overall": image.get("pos_overall", "")
        })

# Create a DataFrame directly from the extracted data
df = pd.DataFrame(all_images)

# Save to CSV
df.to_csv("google_images.csv", index=False)
print("Successfully saved all images.")
```
This code saves only the ```organic``` search results. If you expect paid/sponsored image results, make sure to add logic that additionally saves the ```paid``` results from the API response.

## Complete Google Image scraper example

Let’s put all the code together:

```python
import requests
import pandas as pd


USERNAME = "your_API_username"
PASSWORD = "your_API_password"

payload = {
    "source": "google_search",
    "query": "cute cat",
    "geo_location": "United States",
    "context": [
        {"key": "tbm", "value": "isch"},
    ],
    "parse": True,
    "pages": 2
}

response = requests.post(
   "https://realtime.oxylabs.io/v1/queries",
   auth=(USERNAME, PASSWORD),
   json=payload
)

response_data = response.json()

all_images = []
for page in response_data["results"]:

    organic_results = page["content"]["results"]["organic"]

    for image in organic_results:
        all_images.append({
            "title": image.get("title", ""),
            "link": image.get("link", ""),
            "image": image.get("image", ""),
            "domain": image.get("domain", ""),
            "position": image.get("pos", ""),
            "position_overall": image.get("pos_overall", "")
        })

df = pd.DataFrame(all_images)
df.to_csv("google_images.csv", index=False)
print("Successfully saved all images.")
```

Executing the code will output a CSV file that contains all the Google Image data scraped from two pages:

<img width="2852" height="1426" alt="images_csv" src="https://github.com/user-attachments/assets/18b5688b-2444-4b47-8f8c-7b9aa5b6c6f7" />

Looking to scrape data from other Google sources? [Google Sheets for Basic Web Scraping](https://github.com/oxylabs/web-scraping-google-sheets), [How to Scrape Google Shopping Results](https://github.com/oxylabs/scrape-google-shopping), [Google Play Scraper](https://github.com/oxylabs/google-play-scraper), [How To Scrape Google Jobs](https://github.com/oxylabs/how-to-scrape-google-jobs), [Google News Scrpaer](https://github.com/oxylabs/google-news-scraper), [How to Scrape Google Scholar](https://github.com/oxylabs/how-to-scrape-google-scholar), [How to Scrape Google Flights with Python](https://github.com/oxylabs/how-to-scrape-google-flights),  [Scrape Google Search Results](https://github.com/oxylabs/scrape-google-python), [Scrape Google Trends](https://github.com/oxylabs/how-to-scrape-google-trends)
