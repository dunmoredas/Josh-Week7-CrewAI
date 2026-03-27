import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

load_dotenv()

# Method 2: Use environment variables for LLM config[citation:7]
os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY", "dummy")
os.environ["OPENAI_API_BASE"] = os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

# Your agents (they'll automatically use the env vars above)
market_maven = Agent(
    role="Market Maven",
    goal="Find ALL the tea on AI customer service market - size, players, trends, the whole vibe",
    backstory="""Literally lives for market research. Has 47 tabs open at all times. 
    Sleeps at 3am reading Gartner reports like others read Wattpad. 
    Knows what's trending before it trends. Coffee is their blood type.""",
    verbose=True
)

strategy_wizard = Agent(
    role="Strategy Wizard",
    goal="Turn messy market data into actual actionable strategies that make sense",
    backstory="""Ex-consultant who left McKinsey but still gets excited about frameworks. 
    Makes SWOT analysis actually interesting (yes it's possible). 
    Known for saying 'wait this data is actually telling us something wild' 
    and then explaining it in human language.""",
    verbose=True
)

story_weaver = Agent(
    role="Story Weaver",
    goal="Make executive reports that people actually want to read",
    backstory="""The only person who can explain AI to your aunt at Thanksgiving. 
    Used to write for TechCrunch but got tired of clickbait. 
    Turns complex analysis into narratives that don't put people to sleep. 
    Believes 'professional' doesn't have to mean 'boring af'.""",
    verbose=True
)

# The tasks
task1 = Task(
    description="""Research the AI-powered customer service market in North America. 
    Find actual numbers and real trends, not just vibes.
    
    Specifically look for:
    - How big is this market rn? ($ amount)
    - Who are the main players? (top 5 companies)
    - How fast is it growing? (%)
    - What's trending? (3 big things happening)
    - Who's buying this stuff? (customer demographics)
    - Any red flags? (regulations, barriers, etc.)
    
    Make sure you have actual data points, not just 'it's growing fast'.""",
    expected_output="""Market research doc with:
    - Market size and growth projections (with numbers)
    - Competitor rundown (names + market share)
    - 3-5 key trends with explanations
    - Customer profile (who, why, how much they spend)
    - SWOT style analysis of the opportunity
    - Citations/sources (even if estimated, say where from)""",
    agent=market_maven
)

task2 = Task(
    description="""Take the research and figure out what it actually means for business strategy.
    
    You need to give:
    - Is now the right time to enter this market? (yes/no and why)
    - What's the smartest way to do it? (acquisition, build in-house, partnership?)
    - What could go wrong? (risks and how to deal with them)
    - How much money are we talking? (ballpark investment and potential returns)
    - What makes companies succeed or fail here?
    
    Be honest about risks - don't just paint a pretty picture.""",
    expected_output="""Strategic analysis including:
    - Feasibility assessment (can we do this?)
    - Recommended approach (with reasoning)
    - Risk analysis (bad stuff that could happen + backup plans)
    - Resource needs (people, money, time)
    - Financial projections (low, medium, high scenarios)
    - Key success factors (what winners do differently)""",
    agent=strategy_wizard,
    context=[task1]
)

task3 = Task(
    description="""Create the final executive report. Make it professional but not boring.
    
    Structure it like:
    1. TL;DR version (executive summary - 1 page max)
    2. The opportunity (what we found)
    3. The strategy (what we should do)
    4. Risks and how we handle them
    5. Next steps (literally what happens Monday)
    
    Keep it concise but don't skip important details. 
    Execs need to make decisions from this, so make it clear what they should do.""",
    expected_output="""Executive report with:
    - Title page (topic, date, who it's for)
    - Executive summary (1 page, all the key points)
    - Market analysis section (what we learned)
    - Strategic recommendations (what we should do)
    - Implementation plan (how we do it, timeline)
    - Risk management (what could go wrong)
    - Call to action (literally what to do next)""",
    agent=story_weaver,
    context=[task1, task2]
)

# Set up the crew
crew = Crew(
    agents=[market_maven, strategy_wizard, story_weaver],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"topic": "AI-Powered Customer Service Solutions in North America"})
print(result)
