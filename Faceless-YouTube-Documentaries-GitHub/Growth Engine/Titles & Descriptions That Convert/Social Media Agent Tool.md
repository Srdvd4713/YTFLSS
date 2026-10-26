# Social Media Agent (LangChain)
**GitHub:** https://github.com/langchain-ai/social-media-agent
**Stage:** Automated Social Distribution

## What It Does
Turn a URL into ready-to-publish social media posts:
- Auto-drafts X (Twitter) and LinkedIn posts
- Human review + edit step built in
- Schedules posts through AI agent workflow

## Workflow for Documentary Channel
1. Input: Your new YouTube video URL
2. Agent generates: X thread + LinkedIn post
3. You review / approve / edit
4. Agent schedules and publishes

## Post Templates to Pre-load

### X (Twitter) — Hook Post
> "The [SUBJECT] you thought you knew is nothing like the truth.
> 
> We spent [X] hours researching what really happened.
> 
> Full documentary ? [LINK]"

### LinkedIn — Insight Post
> "Most people don't know that [SHOCKING FACT].
>
> We documented the full story of [TOPIC] — including [KEY REVELATION].
>
> Watch the full 20-minute documentary here: [LINK]"

## Notes
- LangChain-native = easily customizable
- Store your best post templates in Automation & Systems\Prompt Libraries
- Use for every upload day = consistent distribution without extra work
