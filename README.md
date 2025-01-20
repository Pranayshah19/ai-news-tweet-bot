# AI/ML Tech News Tweeter

This project is an automated system that fetches AI/ML/Tech-related news, summarizes it, and tweets an engaging post. It uses various APIs and orchestrates multiple agents to accomplish this task seamlessly.

## Project Overview
The system consists of five main components:
1. **NewsFetcherAgent**: Fetches the most popular AI/ML/Tech-related news article.
2. **ContentSummarizerAgent**: Summarizes the content of the news article.
3. **TweetCraftingAgent**: Crafts a concise and engaging tweet from the summary.
4. **TwitterPostingAgent**: Posts the crafted tweet to Twitter.
5. **ArticleManagerAgent**: Manages the history of posted articles to avoid reposting the same content.

---

## Features
- Fetches the latest popular AI/ML/Tech-related news using the **News API**.
- Summarizes the article using **Gemini Generative AI**.
- Crafts engaging tweets with constraints such as character limits and hashtags.
- Posts tweets to **Twitter** using the Twitter API.
- Maintains a log of posted articles to prevent duplicate tweets.

---

## Prerequisites
### Required API Keys:
1. **News API Key**: Sign up at [News API](https://newsapi.org/) to get your API key.
2. **Gemini Generative AI Key**: Obtain your API key from your Gemini Generative AI account.
3. **Twitter API Keys**: Create a developer account at [Twitter Developer Platform](https://developer.twitter.com/) and generate the following:
   - API Key
   - API Secret
   - Access Token
   - Access Token Secret

### Install Required Libraries
Install the necessary Python libraries using:
```bash
pip install requests requests-oauthlib google-generativeai
```

---

## File Structure
- **main.py**: The core script orchestrating the entire pipeline.
- **posted_articles.json**: A file storing hashes of already posted articles.

---

## How It Works
1. **Fetch News**:
   The `NewsFetcherAgent` retrieves the most popular AI/ML/Tech-related news article from News API.

2. **Summarize Content**:
   The `ContentSummarizerAgent` sends the article’s title and content to Gemini AI, which returns a concise summary.

3. **Craft Tweet**:
   The `TweetCraftingAgent` generates an engaging tweet that:
   - Is concise.
   - Includes emojis and hashtags.
   - Adheres to Twitter’s character limits.

4. **Post Tweet**:
   The `TwitterPostingAgent` posts the crafted tweet to Twitter.

5. **Log Posted Article**:
   The `ArticleManagerAgent` saves the article’s hash in `posted_articles.json` to ensure no duplicates are posted.

---

## Running the Project
1. Save the script as `main.ipynb`.
2. Create a file named `posted_articles.json` in the same directory and initialize it with:
   ```json
   {
       "articles": []
   }
   ```
3. Replace the placeholders in the script with your API keys:
   ```python
   NEWS_API_KEY = "your_news_api_key"
   GEMINI_API_KEY = "your_gemini_api_key"
   TWITTER_API_KEY = "your_twitter_api_key"
   TWITTER_API_SECRET = "your_twitter_api_secret"
   TWITTER_ACCESS_TOKEN = "your_twitter_access_token"
   TWITTER_ACCESS_TOKEN_SECRET = "your_twitter_access_token_secret"
   ```
4. Run the script:
   ```bash
   python main.py
   ```

---

## Example Output
### Console Output:
- **When a new article is found**:
  ```
  Crafted Tweet:
  AI is revolutionizing the world! Read more: https://example.com/article #AI #ML #TechNews

  Tweet posted successfully!
  ```

- **When an article has already been posted**:
  ```
  Article already posted. Exiting.
  ```

---

## Limitations
- Requires valid API keys for all services.
- Limited by API rate limits (e.g., News API and Twitter API).
- Summarization depends on the accuracy of Gemini Generative AI.

---

## Future Enhancements
- Integrate advanced summarization using models like OpenAI’s GPT.
- Support for multiple articles in one run.
- Error handling and retries for API failures.
- Add more hashtags or dynamic hashtag generation based on the article’s content.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it for your purposes.

---

## Acknowledgments
- [News API](https://newsapi.org/) for providing access to news articles.
- [Gemini Generative AI](https://www.example.com) for summarization capabilities.
- [Twitter Developer Platform](https://developer.twitter.com/) for enabling tweet posting.

