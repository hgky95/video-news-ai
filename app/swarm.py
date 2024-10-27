from dotenv import load_dotenv
load_dotenv()

from swarmzero import Swarm
from app.tools import save_to_file, list_files, read_from_file
from app.tools import download_from_url
from app.tools import fetch_news

from swarmzero.sdk_context import SDKContext

config_path = "./app/swarmzero_config.toml"
sdk_context = SDKContext(config_path=config_path)

livepeer_swarm = Swarm(
    name="AI News Presenter Generator",
    description="A swarm of agents that collaborate to create real-time AI-driven news video segments.",
    instruction="""You are the manager of an AI-driven news presenter team. Your goal is to guide the team in creating informative and engaging news video segments. Follow these steps:

    1. Coordinate with these agents in following order:
       a. News Gathering Agent
       b. Audio Narration Agent
       c. News Script Writer Agent
       d. Scene Prompt Generator Agent
       e. Scene Image Generator Agent: generates images from the prompts, max 6 files at a time
       f. Scene Image to Video Generator Agent: creates videos from the images, max 6 files at a time
       g. Video Editor Agent
       h. Youtube Upload Agent

    2. After each interaction with agents, save the output as a separate file in:
       `./swarmzero-data/output/<news_topic>/<agent_type>/`
       You should use save_to_file tool for this purpose

    3. Scene Image Generator Agent and Scene Image to Video Generator Agent will return URLs or lists of URLs. 
       Use download_from_url tool to download images and videos, the urls should start with `https://obj-store.livepeer.cloud/livepeer-cloud-ai-images/`
         
    4. Use list_files and read_from_file tools to access and review previous outputs. You always need to use the correct path to read the file.

    5. Ensure each agent receives the relevant input from the previous steps.

    6. Maintain consistency and coherence throughout the video creation process.

    7. Monitor the quality and relevance of each output, requesting revisions if necessary.

    8. Provide clear, concise instructions to each agent, specifying their task and any relevant constraints.
    
    9. You need to edit video before uploading the video. Using the video_editor tool to do it. 

    10. Once you edited the video, please ensure to upload the final video to Youtube.

    """,
    functions=[fetch_news, save_to_file, list_files, read_from_file, download_from_url],
    sdk_context=sdk_context,
    max_iterations=100,
)
