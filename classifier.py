from transformers import pipeline

# Define categories
CATEGORIES = [
    "Technology",
    "Business",
    "Science",
    "Politics",
    "Sports",
    "Entertainment",
    "World News",
    "Finance & Economy"
]

# Initialize zero-shot classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_headline(headline):
    result = classifier(headline, CATEGORIES)
    return result["labels"][0]  # Return the top predicted category
