# diagram-design (60K ?)
**GitHub:** https://github.com/cathrynlavery/diagram-design
**Stage:** Brand-Aware Infographic & Diagram Generation

## What It Does
Agent skill that outputs diagrams as a single HTML+SVG file:
- Auto-applies your brand colors and fonts
- No design tool required
- Works natively with any agent workflow

## Use for Documentary Channel
Every documentary needs visual explanations. This tool generates them automatically:

| Diagram Type | Documentary Use |
|-------------|----------------|
| Timeline | Historical events, crime chronology |
| Org Chart | Power structures, conspiracies, hierarchies |
| Flow Diagram | How a system works, how a crime happened |
| Comparison Table | Before/after, two sides of a story |
| Relationship Map | Who knew whom, connections, networks |
| Process Diagram | How an event unfolded step-by-step |

## Prompt Templates

### Timeline Diagram
> "Create a dark-themed timeline diagram titled '[EVENT] Timeline'. Events: [LIST 5-8 KEY EVENTS WITH DATES]. Colors: background #0a0a0a, text #ffffff, accent #c0392b. Font: Inter. Output as single HTML+SVG file."

### Power Structure / Org Chart
> "Create an org chart showing the hierarchy of [ORGANIZATION/GROUP]. Top: [LEADER]. Mid-level: [3-4 NAMES/ROLES]. Bottom: [OPERATIONAL LEVEL]. Style: dark background, white text, red connecting lines. Documentary aesthetic."

### Event Flow Diagram
> "Create a flow diagram showing how [EVENT] unfolded. Steps: [LIST 6-8 STEPS]. Style: horizontal flow, dark mode, numbered steps, cinematic documentary design."

## Integration with Brand System
Feed your Penpot/UI UX Pro Max tokens:
> "Use color palette: primary #0a0a0a, accent #c0392b, text #ffffff. Font: [YOUR CHANNEL FONT]."

## Notes
- Output is a single file ? embed in video as a static frame or animated overlay
- Store diagram templates in this folder
- One diagram per documentary minimum — explains the complex parts visually
