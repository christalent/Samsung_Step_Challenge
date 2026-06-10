# Samsung Step Challenge

## Live App

**https://freeshell.de/~talent/step-tracker/** ← the working web app

The `Step Challenge Tracker/` directory in this repo contains the source for the live app.

## What it does

Tracks Samsung Health step challenge progress across multiple years:
- Star challenge tiers by month (6 stars per month, varying step targets)
- Daily step entry and streak tracking
- Completion history and earned star counts per year

## Repo structure

```
Samsung_Step_Challenge/
├── Step Challenge Tracker/
│   ├── index.html        ← source for the live app
│   └── api.php           ← backend
├── Step.py               ← Python tracking scripts
├── Star Challenges by Month.json  ← canonical challenge data
├── Star Challenges by Month.csv
└── Star Challenges by Month.txt
```

## Data source

Challenge tier definitions live in `Star Challenges by Month.json`. The web app reads from this file.
