# Remotion (67K ?)
**GitHub:** https://github.com/remotion-dev/remotion
**Stage:** React-Based Programmatic Video Engine
**Stress-Test Recommendation: #1 — START HERE**

## What It Does
Build videos with React components:
- Programmatic, fully reproducible
- Dynamic data-driven motion graphics
- Official agent skill repo (teaches LLMs to use it)
- Output: MP4, GIF, image sequences

## Why This Is Your #1 Tool
Every documentary needs the same assets every episode:
- Animated intro/outro
- Chapter cards
- Lower thirds (expert names, source citations)
- Stat/data reveals
- End screen

Remotion lets you build these ONCE as React components, then generate them for every episode automatically.

## Key Components to Build

### 1. Documentary Intro
```jsx
export const DocIntro = ({ title, episode, channelName }) => (
  <AbsoluteFill className="bg-black">
    <Sequence from={0} durationInFrames={60}>
      <FadeIn><ChannelLogo /></FadeIn>
    </Sequence>
    <Sequence from={60} durationInFrames={90}>
      <SlideUp><h1>{title}</h1></SlideUp>
    </Sequence>
  </AbsoluteFill>
);
```

### 2. Chapter Card
```jsx
export const ChapterCard = ({ number, title, timestamp }) => (
  <AbsoluteFill className="chapter-bg">
    <div className="chapter-number">Chapter {number}</div>
    <div className="chapter-title">{title}</div>
    <div className="timestamp">{timestamp}</div>
  </AbsoluteFill>
);
```

### 3. Expert Lower Third
```jsx
export const LowerThird = ({ name, title, org }) => (
  <div className="lower-third slide-up">
    <span className="name">{name}</span>
    <span className="title">{title} — {org}</span>
  </div>
);
```

### 4. Stat Reveal
```jsx
export const StatReveal = ({ value, label, source }) => (
  <AbsoluteFill className="stat-bg">
    <CountUp end={value} className="stat-value" />
    <p className="stat-label">{label}</p>
    <small className="stat-source">{source}</small>
  </AbsoluteFill>
);
```

## Setup
```bash
npx create-video@latest
cd my-video
npm run dev   # preview in browser
npm run build # render MP4
```

## Agent Skill Repo
The official skills repo teaches Claude/Codex how to write Remotion code.
Point your agent at: https://github.com/remotion-dev/remotion (skills/ folder)

## Notes
- Build your component library once, generate forever
- Every episode = same components, new data
- Pair with HyperFrames for full HTML+video pipeline
