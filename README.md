# AI-driven news video generator
This project leverages SwarmZero AI and Livepeer AI to create an AI-driven news video generator. The system starts with a News Aggregator Agent that fetches real-time news from external APIs. The Audio Narration Agent converts news descriptions into speech, and a series of agents—Scene Prompt Generator, Image Generator, and Image-to-Video Generator—create engaging visuals. These images and narration are combined into short video segments through the Video Editor Agent. Finally, the video is uploaded to YouTube via the YouTube Upload Agent. The project automates content creation, using AI and decentralized media pipelines, allowing for seamless generation of news videos and offering a unique tool for creators.

The SwarmZero AI allows user to use their preferred LLM model from OpenAI (gpt4, gpt4o, etc), Anthropic (3.5 sonnet, etc) or other open source LLMs by simply defining the model name in the configuration.

## Swarm Agents - Workflow
![video-news-ai drawio](https://github.com/user-attachments/assets/c2976ada-4672-46f1-a931-3af0036b90e9)

## Requirements

- Python 3.11
- OpenAI Key or open-source LLM
- Livepeer AI Key
- Google API Client
- TheNewsAPI Key

## Setup your Google API Client
To set up YouTube API credentials, go to the Google API Console, create a new project, enable the YouTube Data API v3, and set up OAuth 2.0 credentials by configuring a consent screen and adding valid redirect URIs (http://localhost:8088/) and (http://localhost:8088/flowName=GeneralOAuthFlow) for authentication. 

Download the client_secret.json file and place it in your project’s root directory to handle secure OAuth 2.0 authentication, which is necessary for authorizing API requests and accessing private YouTube data securely. Also, register yourself as a test user in the OAuth Consent Screen.

## Installation
1) Clone the repository
2) Go to video-news-ai folder
3) Setup Python virtual environment: `python -m venv .venv`
4) Activate virtual environment:

    On Windows: `.venv\Scripts\activate`

    On Unix or MacOS: `source .venv/bin/activate`
6) Install library dependencies: `pip install -r requirements.txt`

## Setup Environment Variables
1) Create .env file: `touch .env`
2) Add API keys to .env file:
```
MODEL=gpt-4-turbo-preview
OPENAI_API_KEY=
MISTRAL_API_KEY=
ANTHROPIC_API_KEY=
ENVIRONMENT=dev
SWARMZERO_LOG_LEVEL=INFO
SWARMZERO_DATABASE_URL=
PINECONE_API_KEY=
LIVEPEER_API_KEY=
NEWS_API_KEY=
```

## Run the app
- Run the agent: `(venv) python main.py`
- Input your prompt: `Create a short video from the two latest news`

## Result
- Video uploaded shows in the console as below:
<img width="1313" alt="Screen Shot 2024-10-19 at 09 12 39" src="https://github.com/user-attachments/assets/1821894a-5536-4627-b284-a5e3f9e7114d">
- Go to YouTube (short video), you will see the new video:
<img width="1313" alt="short video" src="https://github.com/user-attachments/assets/594f0a10-ac85-407a-a217-1ab170ef27b6">

## Acknowledgement
This project is an extension of [Swarm example](https://docs.swarmzero.ai/examples/swarms/livepeer-youtube-video-generator-swarm) from SwarmZero.ai.
