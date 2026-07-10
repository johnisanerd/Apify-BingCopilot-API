"""
Bing Copilot API: A Quick Start Example
See more at: https://apify.com/johnvc/bing-copilot-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/bing-copilot-api/input-schema?fpr=9n7kx3

This script shows how to call the Bing Copilot API on Apify from Python and read
its structured JSON output. It exercises several input parameters so you can see
what is configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input. Values are kept small to keep this first run cheap.
run_input = {
    # One or more questions to resolve. Batch several into one run.
    "queries": ["best crm for startups", "best help desk software"],
    # Optional: track whether a brand is named. Adds a "brandMentioned"
    # boolean to every answer row.
    "brandToTrack": "Acme",
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/bing-copilot-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id)
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} item(s).\n")

for item in items:
    print(item.get("query"),
          "| answer present:", item.get("answerPresent"),
          "| brand mentioned:", item.get("brandMentioned"),
          "| references:", len(item.get("references") or []))
