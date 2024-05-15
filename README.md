# How To Scrape Google Images

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

Real time google image scraper. The process is automated by sending HTTP requests to retrieve image data which is then parsed and saved. 

## Scrape Google Images using Oxylabs’ Google Images Scraper API


For this tutorial, we will use [Google Images Search API](https://oxylabs.io/products/scraper-api/serp/google/images) to get the Google images related to the one given in the query. This API helps us retrieve all the related images and the URLs (where these images are hosted).  

To use this API, you must create an account on Oxylabs and get the API credentials. These credentials will be used in the later stages.

Step 1 - Setting up the environment
To get started, we must have Python 3.6+ installed and running on your system. Also, we need the following packages to put our code into action:

requests - for sending HTTP requests to Oxylabs API.

Pandas - for saving our output data in dataframes and saving in CSV files. 

To install these packages, we can use the following command:
