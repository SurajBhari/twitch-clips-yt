# twitch-clips-yt

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white)
![Twitch](https://img.shields.io/badge/Twitch-9146FF?style=flat&logo=twitch&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube&logoColor=white)
![status](https://img.shields.io/badge/status-WIP-yellow?style=flat)

A Twitch clip scraper, built toward the "Twitch clips → YouTube" content pipeline that many faceless channels run.

## The idea

Fetch the most recent clips from the Twitch channels you're subscribed to, download them, and (eventually) auto-process and re-upload them to YouTube as Shorts/compilations — trimmed, cropped, and length-filtered.

> Plenty of channels [do exactly this](https://www.youtube.com/results?search_query=twitch+clips); this was an attempt at automating the boring parts.

## Status

| | |
|---|---|
| ✅ Done | Fetching the most recent clips from subscriptions and downloading them. |
| 🚧 To do | Auto-trim/crop into short videos and post them to YouTube. |

## How it works

Uses Selenium (Firefox) with exported cookies for both Twitch and YouTube (`cookies-twitch.json`, `cookies-yt.json`) to browse subscriptions, pull recent clips into `data.json`, and download them.

## Run

```bash
pip install -r requirements.txt
python main.py
```

Provide your exported Twitch/YouTube cookies as JSON before running.
