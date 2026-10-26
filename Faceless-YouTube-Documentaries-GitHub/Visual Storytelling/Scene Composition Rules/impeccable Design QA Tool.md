# impeccable (85K ?)
**GitHub:** https://github.com/pbakaus/impeccable
**Stage:** Design Quality Control — 62-rule AI-slop checker

## What It Does
Runs 62 rule-based automated checks on any design output:
- Spacing rhythm violations
- Type hierarchy mismatches
- Color contrast failures (WCAG)
- Layout proportion errors
- Visual noise / clutter flags

## Use as Your QA Gate
Run every thumbnail, title card, and graphic through this before publishing.

## Checks Most Relevant for Thumbnails
- Text contrast ratio (min 4.5:1)
- Alignment to invisible grid
- Margin consistency
- Font size hierarchy (H1 > H2 > body rule)
- Color count (max 3 dominant colors)

## Workflow
1. Generate asset (FLUX.2, Penpot, HyperFrames)
2. Run impeccable check
3. Fix flagged items
4. Approve and publish

## Notes
- Add custom rules for your channel's visual standards
- Store approved configs in this folder
