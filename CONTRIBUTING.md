# Contributing to Free Datasets
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Start new dataset
- Add new data to already created dataset
- Do data analysis

## How to add a new dataset

### Create a new issue
To create a new dataset, create an issue using the issue template and wait for approval. The dataset you want to create it must be a text dataset (json, csv, xml, etc), which means no image or video datasets are allowed, because we can make the repository easy to clone.

### Create a dataset folder
Once approved, you need to create a new folder in the format `word-word-word` for your dataset in the dataset folder at the root of this project.

### Create a REAMDE for you dataset
It is necessary to create a `README` file for your datasat to tell people what kind of data you are creating and how it is structured. For this `README.md` we recommend adding the following information:
- **Description**: Explain what type of data you are storing
- **Format**: Explain how you structure your dataset, for example: store all data in a `.csv` or separate file.
- **Source(optional)**: If you get the information from web scraping or any public source, please add a link to the page from where you collect the information.
- **Example**: Please provide a simple dataset sample.

If you think it's important to add more information to `README.md`, feel free to add it.

### Create Merge request with the new dataset
It's time to merge the new dataset with the repository. Open a Merge request and wait for approval or feedback.

**Note: If you add your dataset(s), you agree to share your data publicly and allow people to use it.**

### Consideration about your dataset
There are a few considerations before adding a new dataset:
- The dataset you want to push to this repository must be new. You cannot copy an already created dataset and load it.
- Do not upload private information of people (emails, credit cards, social number, etc.).
- Your dataset must have a minimum of 50 records (to allow people who want to perform data analysis on your dataset).
- The dataset must be real data.

## How to add new data to an already created dataset

### Find a dataset
Find an interesting dataset you want to collaborate on and you can insert more information

### Check dataset format and data
You must follow the structure and types of the data set.

### Update datset
Once you have the new records for the dataset, update the dataset file and, if necessary, update the `README` file.

**Note: If you add your data to dataset(s), you agree to share your data publicly and allow people to use it.**

## How to do data analysis

To get started, create a new folder in the format `word-word-word` in the `data analysis` folder. The analysis you will do will need to use the dataset in this repository and it must be accessed by a realtive path (do not copy the dataset into your folder). When you finish your analysis, write a `README` file specifying:
- what was the purpose
- how did you do it
- What was the results?

### Consideration about your analysis
There are some considerations for your analysis:
- Try to use languages like Python and R
- Specify what libraries you used
- Avoid to do only a simple analysis like average values.
