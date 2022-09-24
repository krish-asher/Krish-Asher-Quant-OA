# Reddit Subreddit Scraper

**Difficulty: 3**

Thank you for applying to Quant! We are interested in your application and want to see what you can do with the skills and knowledge you possess. Please read through the following prompt for directions.

## **Prompt: Reddit Subreddit Scraper**
The rise of retail trading and tracking this information dessimination has often been at the center of attention for those looking to place trades on this information. Reddit has been in the news lately in regards to how groups of retail traders are able to share their market sentiments through its communications platform. We want to be able to use this information to unleash insights into our positions.

Your task is to build a Python scraper for Reddit using its API. The goal of this script will be to gather information about pertinent subreddits that we can use later as part of our Quantitative Research and Strategy Implementation divisions. Your scrape should gather data about a subreddit, namely the number of accounts less than 3 months old, the top posts for every week for the last 26 weeks, the top 10 replies to those post, and the posts' information (i.e., up/down votes, replies, etc.). We need to be able to parse this information, maybe as dataclass objects, and then the data needs to be output into a fast, parsable file format (could be JSON or CSV, for example). 

In addition to the criteria listed below, you will be graded on the time complexity of your code, the ability to "future-proof" it, and its readability for someone unfamiliar with the codebase. This means it would also be wise to include some information on how to run your code, what your code does, and maybe even a section espousing areas for future improvements in case someone else continues your project subsequently.

To start working on your project, **make sure you have forked the repository so that you will own your own version**. If you have any questions, feel free to contact us.

## **Resources**
- https://www.reddit.com/dev/api/
- https://praw.readthedocs.io/en/stable/
- https://www.youtube.com/watch?v=vBH6GRJ1REM

## **Deliverables**
Your python application/script should do the following:
- Be able to accept command line arguments to pass in a subreddit (e.g. "r/wallstreetbets")
- Parse the subreddit to obtain the following information in as few calls as possible:
  - number of accounts < 3 months old
  - the top 5 posts for every week for the last 26 weeks
  - the top 6 replies to each of the above posts
  - any metrics on the posts and replies
  - any additional metrics you think might be useful!
- Store all data into an easily parsable and logical objects
- Output data into a file with logical parsing
- As part of your python application, add a script that will help parse the file with respect to your data class

Optional requirements:
- Create a script that will expose this as an API
- Add your own pyenv with all requirements
- Be able to pass in a txt file with names of subreddits instead of one-by-one
- Be able to use regex to dynamically search for subreddits, ideally in addition to the above bullet.

## **Grading**
We will be looking at your project and grading it under these five criteria:
1. Code
   - If it works
   - Modular
   - Follows best practices (ie. OOP)
2. Documentation
   - Concise and exact
   - Follows popular conventions
3. Styling
   - Human readable
   - Can quickly glance to receive all relevant information
   - Follows Google Style Guide (preferred if it exists) or most popular convention (ie. PEP8)
4. Robustness
   - Customizable
   - No technical debt (future proof)
   - Handles bad inputs and errors
5. Git
   - [Good commit messages](https://cbea.ms/git-commit/#seven-rules)
   - Commits are properly sized

For a full list of the grading criteria, please see the following [document](https://docs.google.com/spreadsheets/d/16CqSJSlch7w9q4_ZTiydKGk0T01rgvIEcHHwqsI_KSo/edit?usp=sharing). 
