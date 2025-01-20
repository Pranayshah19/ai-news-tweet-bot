from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Request model
class NewsRequest(BaseModel):
    text: str

# Response model
class NewsResponse(BaseModel):
    word_count: int
    summary: str

@app.post("/process_news", response_model=NewsResponse)
async def process_news(news: NewsRequest):
    """
    Endpoint to process news text and return a summary and word count.
    """
    if not news.text.strip():
        raise HTTPException(status_code=400, detail="News text cannot be empty.")

    # Calculate word count
    word_count = len(news.text.split())

    # Simple summary logic (just the first sentence for now)
    summary = news.text.split(".")[0] + "."

    return NewsResponse(word_count=word_count, summary=summary)
