# AIML Chatbot

A chatbot built with **AIML** (Artificial Intelligence Markup Language), Python and Flask.

## Features
- Pattern-matching conversation using AIML (`<pattern>`, `<template>`, `<srai>`, `<random>`, `<set>/<get>`)
- Remembers your name and favourite language during a session
- Tech FAQ (AI, ML, NLP, Python, C#, SQL, API, Cloud ...)
- Small talk and jokes
- Two interfaces: command line and web UI

## Setup
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

## Run
```bash
python main.py      # command-line chat
python app.py       # web UI at http://127.0.0.1:5000
```

## Project structure
```
aiml-chatbot/
├── aiml_files/
│   ├── startup.xml       # loads all AIML files
│   ├── basic_chat.aiml   # greetings, identity, fallback
│   ├── tech_faq.aiml     # AI / programming Q&A
│   ├── smalltalk.aiml    # jokes, casual chat
│   └── memory.aiml       # remembers user details
├── templates/index.html
├── static/ (style.css, app.js)
├── bot.py                # AIML kernel wrapper
├── main.py               # CLI
├── app.py                # Flask web app
└── requirements.txt
```

## Adding your own knowledge
Open any `.aiml` file and add:
```xml
<category>
    <pattern>WHAT IS DOCKER</pattern>
    <template>Docker packages apps into lightweight containers.</template>
</category>
```
Then **delete `bot_brain.brn`** (the cached brain) and restart so the new rules load.
Patterns must be UPPERCASE with no punctuation. `*` is a wildcard.

## Sample conversation
```
You  : hello
Bot  : Hi there! What would you like to talk about?
You  : my name is Stuti
Bot  : Nice to meet you, Stuti!
You  : what is my name
Bot  : Your name is Stuti.
You  : what is machine learning
Bot  : Machine learning is a subset of AI where systems learn patterns from data...
```
