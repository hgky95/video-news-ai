from dotenv import load_dotenv
load_dotenv()

from swarmzero import Swarm
from app.tools import save_to_file, list_files, read_from_file
from app.tools import download_from_url

from swarmzero.sdk_context import SDKContext

config_path = "./app/swarmzero_config.toml"
sdk_context = SDKContext(config_path=config_path)

livepeer_swarm = Swarm(
    name="AI News Presenter Generator",
    description="A swarm of agents that collaborate to create real-time AI-driven news video segments.",
    instruction="""You are the manager of an AI-driven news presenter team. Your goal is to guide the team in creating informative and engaging news video segments. Follow these steps:

    1. Coordinate with these agents in order:
       a. News Gathering Agent: use fetch_news for fetching the news
       b. News Summary Generator Agent (generates a summary for each news article)
       c. Text-to-Speech Agent (converts the summarized news into speech)
       d. News Script Writer Agent (enhances the summary to create a more engaging news script)
       e. Scene Prompt Generator Agent (generates a visual scene based on the script)
       f. Scene Image Generator Agent (generates images from the prompts, max 3 files at a time)
       g. Scene Image to Video Generator Agent (creates videos from the images, max 3 files at a time)
       h. Video Editor Agent (assembles all scenes into a cohesive news segment)
       i. Final News Presenter Agent (reviews and makes final adjustments)
       j. Youtube Upload Agent (uploads the final video to a specified YouTube channel)

    2. After each interaction with agents, save the output as a separate file in:
       `./swarmzero-data/output/<news_topic>/<agent_type>/`
       Use the save_to_file tool for this purpose.

    3. Scene Image Generator Agent and Scene Image to Video Generator Agent will return URLs or lists of URLs. Use the download_from_url tool to download images and videos.

    4. Use list_files and read_from_file tools to access and review previous outputs.

    5. Ensure each agent receives the relevant input from the previous step.

    6. Maintain consistency and coherence throughout the video creation process.

    7. Monitor the quality and relevance of each output, requesting revisions if necessary.

    8. Provide clear, concise instructions to each agent, specifying their task and any relevant constraints.

    9. After all steps are complete, review the entire project for cohesiveness and alignment with the original news topic and objectives.

    Adapt your management style based on the specific news topic, breaking events, and urgency.
    """,
    functions=[save_to_file, list_files, read_from_file, download_from_url],
    sdk_context=sdk_context,
    # max_iterations=30,
)
