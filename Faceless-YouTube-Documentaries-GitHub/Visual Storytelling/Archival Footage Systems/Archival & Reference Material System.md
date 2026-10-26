# Archival & Reference Material System
*The channel rule is **no stock footage, ever** (CHANNEL BIBLE). The story is 100% animated. Archival and real-world material is used in two places only: as **drawing reference** for scenes, and **on screen in the real-science segment** (Part 6, explainer Shorts) when a real document makes the point stronger.*

## Allowed uses
| Use | Example | On screen? |
|---|---|---|
| Drawing reference | Photos of SAR teams with headlamps → design of the Tall Ones | No |
| Real document callout | A CPSC generator warning label, a CDC chart | Yes, redrawn or as a cited still |
| Real stat card | "~85 US deaths/year (CPSC)" | Yes, in our own design |
| Historic event mention | 2004 Florida hurricanes CO cluster | Yes, as a map/timeline we draw |

## Rights: what we can show
- **US federal government works** (CDC, CPSC, NOAA, NASA, FEMA, NPS) are generally **public domain** in the US. Still credit the agency and check the page for third-party images (those are not PD).
- **Public-domain archives:** Library of Congress (check each item's rights statement), Internet Archive (check the licence per item), Wikimedia Commons (licence per file, often CC BY/BY-SA: credit required, BY-SA requires sharing alike).
- **News footage/photos:** don't use. Redraw the idea instead.
- **Fair use** is a defence, not a permission. Avoid relying on it.

## Preferred method: redraw
Recreating a chart or diagram in our own style (Oswald, navy/amber palette) with the source cited avoids most rights issues and keeps the visual identity. Use `Visual Storytelling/Scene Composition Rules/diagram-design Infographic Tool.md` or a new `diagram` scene in the render engine.

## Folder and log
```
Productions/S0X <Series>/assets/reference/   # drawing reference only, never rendered
Productions/S0X <Series>/assets/archival/    # cleared items that may appear on screen
```
Log every on-screen item:
| File | Source URL | Owner | Licence / status | Credit line | Used in |
|---|---|---|---|---|---|
| cpsc_label.png | cpsc.gov/... | CPSC (US gov) | Public domain | "Source: U.S. CPSC" | P6 0:42 |

## On-screen credit format
Bottom-left, Consolas, 70% snow, 2 s minimum: `Source: U.S. CPSC, 2022`. Repeat all sources in the description.

## Checklist
- [ ] Item is reference-only OR cleared with a logged licence
- [ ] Credit on screen and in description
- [ ] No real victims' faces or names
- [ ] Redrawn in brand style where possible
