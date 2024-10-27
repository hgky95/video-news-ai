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

1. Clone the repository
2. Go to video-news-ai folder
   `cd video-news-ai`
3. Define environment variables for the backend:
`touch .env`
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
4. Define environment variables for frontend:
`touch ui/.env`
```
NEXT_PUBLIC_BACKEND_API=http://127.0.0.1:8000/chat/
```

## Run the app (two options)
### 1. Run with Docker (recommended)
1. Start the application:
`docker-compose up`

The application is ready on: `http://localhost:3000`
### 2. Run manually
1. Setup Python virtual environment: `python -m venv .venv`
2. Activate virtual environment:

   On Windows: `.venv\Scripts\activate`

   On Unix or MacOS: `source .venv/bin/activate`

3. Install library dependencies: `pip install -r requirements.txt`
4. Run the agent: `uvicorn main:app --reload`

5. Open another terminal and go to the ui folder:
`cd ui`
6. Start the frontend app:
`npm run dev`

The application is ready on: `http://localhost:3000`

## How to use
1. Input prompt: ```Create a short video from the two latest news```

     you can also specify the category such as business, tech, sports, etc.

2. Click on 'Generate' button
3. Wait for few minutes for generating process
4. Open browser and access to your Youtube channel to check the new video
![video-news-ai](https://github.com/user-attachments/assets/f51d175a-4b40-4556-aacb-202183e8ff07)


## Potential improvement:
1. Implement a cron job for scheduled video publishing.
2. Expand distribution to TikTok and Twitter.
3. Add advanced editing features and human-like TTS.
4. Optimize the prompt to ensure the tool runs with stability.

## Acknowledgement
[SwarmZero.ai](https://swarmzero.ai/): a decentralized platform designed to empower AI researchers, machine learning engineers, and agent builders

[Livepeer AI](https://www.livepeer.org/): a foundational infrastructure for limitless video computing, enabling AI processing and transcoding jobs to power the future of video
