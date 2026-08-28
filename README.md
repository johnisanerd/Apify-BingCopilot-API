# 🤖 Bing Copilot API: track Microsoft's AI answers and whether they cite your brand, as clean JSON

> The most efficient, reliable, and developer-friendly way to use the Bing Copilot API.

**Actor page:** [apify.com/johnvc/bing-copilot-api](https://apify.com/johnvc/bing-copilot-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/bing-copilot-api/input-schema](https://apify.com/johnvc/bing-copilot-api/input-schema?fpr=9n7kx3)

This API resolves any query to Bing Copilot's AI answer: the headline summary, the full structured answer (headings, lists, tables, code), every cited reference, and an optional brand-mention check. It is built for answer engine optimization (AEO) and generative engine optimization (GEO): tracking what Microsoft's answer engine says, which sources it trusts, and whether your brand shows up. It is the Bing engine in a four-part AEO suite alongside [Google AI Overview](https://apify.com/johnvc/Google-AI-Overview-API?fpr=9n7kx3), [Naver AI Overview](https://apify.com/johnvc/naver-ai-overview-api?fpr=9n7kx3), and [Brave AI Mode](https://apify.com/johnvc/brave-ai-mode-api?fpr=9n7kx3).

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-BingCopilot-API.git
   cd Apify-BingCopilot-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python bing-copilot-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python bing-copilot-api-example.py
```

## Why Use This Bing Copilot API?

AEO and GEO brand monitoring: is your brand cited when Copilot answers your category questions? Track it weekly across your whole keyword set.

Citation-source analysis: which domains does Microsoft's answer engine trust? Target those for PR and content placement.

Competitor share-of-voice: run the same query list with each competitor as brandToTrack and compare mention rates.

Answer-drift tracking: store the markdown over time and diff how the AI answer changes after your content updates.

## Features

### Core Capabilities
- Microsoft's AI answer for any query, as structured JSON
- The full answer as text blocks (paragraphs, headings, lists, tables, code) and a single markdown document
- Every cited reference with title, link, snippet, and source name
- An optional brandMentioned boolean when you set brandToTrack
- A one-line summary and featured media links when present

### Data Quality
- The answer, its citations, and the brand check in one structured row
- Batch a whole keyword set in one run, one charge per query
- Markdown output ready for diffing and LLM pipelines
- The fourth engine in an AEO suite: same input and output shape as the Google, Naver, and Brave answer engines

## Usage Examples

### Basic Example
```json
{
  "queries": ["best crm for startups"]
}
```

### Advanced Example
```json
{
  "queries": ["best crm for startups", "top crm software 2026"],
  "brandToTrack": "Acme"
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `queries` | `list[str]` | YES* | - | The question(s) to resolve. Batch several into one run. |
| `query` | `str` | YES* | - | A single question, as an alternative to `queries`. At least one of `query` or `queries` is required. |
| `brandToTrack` | `str` | no | - | Optional brand name. Adds a `brandMentioned` boolean to every answer row. |

*At least one of `query` or `queries` is required.

## Output Format

```json
{
  "result_type": "copilot_answer",
  "query": "best crm for startups",
  "answerPresent": true,
  "answerHeader": "The best CRM for startups depends on budget and team size, with HubSpot, Pipedrive, and others among the most recommended.",
  "markdown": "## Top CRM picks\n\n- HubSpot: generous free tier\n- Pipedrive: pipeline-first UX",
  "references": [
    { "index": 0, "title": "Best CRMs for Startups (2026)", "link": "https://example.com/best-crms", "source": "Example" }
  ],
  "brandToTrack": "Acme",
  "brandMentioned": false,
  "summary": "The best CRM for startups depends on budget and team size...",
  "fetched_at": "2026-07-10T22:10:00+00:00"
}
```

---

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Bing Copilot API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings > Connectors** (or **Settings > Developer > Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/bing-copilot-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Bing Copilot API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/bing-copilot-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/bing-copilot-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Bing Copilot API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings > Connectors > Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/bing-copilot-api`.
3. In any chat, open **+ > Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/bing-copilot-api`, using OAuth when prompted.
5. Ask Claude to run the Bing Copilot API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/bing-copilot-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/bing-copilot-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor > Settings > MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Bing Copilot API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/bing-copilot-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

## n8n integration

Prefer [n8n](https://n8n.io)? This API is also available as a community node, **[n8n-nodes-bing-copilot-api](https://www.npmjs.com/package/n8n-nodes-bing-copilot-api)**. In n8n, go to **Settings > Community Nodes**, install `n8n-nodes-bing-copilot-api`, then use it in any workflow. It also works as an AI Agent tool.

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Bing Copilot API to power your data workflows with reliable, structured results.*

Last Updated: 2026.08.28
