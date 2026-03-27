# Prompt Log

### User
yo need help with this crewai assignment for my business analytics class. lowkey stressing rn cuz i left it last minute 😭 got till midnight. here's the pdf: [attached mini-assignment-03-crewai-basics.pdf]
can u help me figure out what business problem to pick? something interesting not boring af

### AI
I'd be happy to help! For a CrewAI assignment, you'll want a business problem that allows your three agents to work sequentially. Some interesting options:
- AI-powered customer service market analysis
- Sustainable fashion industry trends
- Electric vehicle adoption barriers
- Remote work software competitive landscape

Which of these sounds most interesting to you?

### User
bet the AI customer service one sounds fire. my prof said we should pick something we'd actually wanna read about so that works. but fr i need to make 3 agents right? like researcher, analyst, writer? thats so basic tho. can i make them sound less boring?

### AI
Absolutely! You can make the roles more engaging while keeping their functions clear. Instead of generic titles, try:
- Market Maven (instead of just Researcher) - someone who's always digging into trends
- Strategy Wizard (instead of Analyst) - turns data into gold
- Story Weaver (instead of Writer) - makes reports actually readable

Would you like me to help you develop these with more interesting backstories?

### User
omg yesss that's so much better!! i want them to have like actual personalities u know? like one could be a coffee-obsessed data nerd who's always up at 3am reading market reports. make them sound like real people not robots

### AI
I love that energy! Let me create some personality-rich agents:

1. **Market Maven** - "Coffee-fueled trend spotter who spends nights scrolling through market reports like others scroll TikTok. Has a sixth sense for spotting what's about to blow up before it hits LinkedIn."

2. **Strategy Wizard** - "Former consultant who quit the corporate grind but still gets hyped about SWOT analyses. Lives for turning messy data into 'wait that actually makes sense' moments."

3. **Story Weaver** - "The friend who can explain crypto to your grandma. Makes complex stuff sound like a Netflix docuseries. Executive reports that don't put people to sleep."

Want me to flesh these out with actual goals and backstories for the code?

### User
yesss this is perfect!! okay now for the tasks... how do i make them not sound like AI wrote them? my prof said "context dependencies" and im like ???

### AI
lmao fr context dependencies just means each task uses what the last one did. think of it like:
- Task 1: Research (finds the tea ☕️)
- Task 2: Analysis (spills the tea in a useful way)
- Task 3: Report (writes the tea summary)

So Task 2 gets Task 1's output, Task 3 gets both. Lowkey simple when you think about it like that.

Want me to write the task descriptions with that same energy?

### User
pls do but make them sound like actual assignment instructions not just memes lol. i still need to pass 💀

### AI
Got you! Here's what I'm thinking:

**Task 1 (Market Maven):** 
"Do a deep dive on AI customer service market. Find out who's winning, who's sleeping, and what's next. Numbers matter - come back with actual stats not just vibes."

**Expected output:** 
"Market research dump with: market size ($X billion), top 5 players, growth rate, and 3 emerging trends. Make it detailed enough that Task 2 can actually work with it."

**Task 2 (Strategy Wizard):** 
"Take the research and figure out what it MEANS. If a company wanted to jump in, where should they go? What's the move? Include risks (don't sugarcoat) and money stuff."

**Expected output:** 
"Strategy breakdown with: SWOT analysis, recommended entry strategy, risks and how to avoid them, and money projections. Make it actionable."

**Task 3 (Story Weaver):** 
"Turn all this into a report that doesn't make executives want to yeet themselves out a window. Keep it professional but actually readable. Start with the TL;DR, end with 'do this next'."

**Expected output:** 
"Executive report with: executive summary, key findings, recommendations, and next steps. 3-5 pages worth but not actually that long."

This vibe work for you?

### User
yesss okay we vibing. now can u give me the actual code? my brain is fried from studying for midterms

### AI
Say less. Here's the code with your agents:

```python
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(
    model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
    base_url=os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com"),
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

# Your iconic agents
market_maven = Agent(
    role="Market Maven",
    goal="Find ALL the tea on AI customer service market - size, players, trends, the whole vibe",
    backstory="""Literally lives for market research. Has 47 tabs open at all times. 
    Sleeps at 3am reading Gartner reports like others read Wattpad. 
    Knows what's trending before it trends. Coffee is their blood type.""",
    llm=llm,
    verbose=True
)

strategy_wizard = Agent(
    role="Strategy Wizard",
    goal="Turn messy market data into actual actionable strategies that make sense",
    backstory="""Ex-consultant who left McKinsey but still gets excited about frameworks. 
    Makes SWOT analysis actually interesting (yes it's possible). 
    Known for saying 'wait this data is actually telling us something wild' 
    and then explaining it in human language.""",
    llm=llm,
    verbose=True
)

story_weaver = Agent(
    role="Story Weaver",
    goal="Make executive reports that people actually want to read",
    backstory="""The only person who can explain AI to your aunt at Thanksgiving. 
    Used to write for TechCrunch but got tired of clickbait. 
    Turns complex analysis into narratives that don't put people to sleep. 
    Believes 'professional' doesn't have to mean 'boring af'.""",
    llm=llm,
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

# Run it
result = crew.kickoff(inputs={"topic": "AI-Powered Customer Service Solutions in North America"})
print(result)
```
That should work! Just make sure your .env has your DeepSeek API key. Need anything else?

### User
ur actually a lifesaver. one more thing tho - i need to make a prompt-log.md file. do i just copy our whole convo? like everything including this?

### AI
Yep! The assignment says "complete, unedited chat history" so just copy everything from the start. That includes:
- Your first message with the PDF
- All my responses
- This convo too

Don't delete anything or summarize it. They want to see the whole process, including the messiness lol. Just paste it all into prompt-log.md exactly as it appears.

Also pro tip: when you run the code, save the output with:
```bash
python crew.py > output.txt 2>&1
```

### User
bet thank u so much!! gonna go run this rn. hope my api key works 💀

### AI
fingers crossed! if it doesn't work, check:
1. .env file exists and has the right variable names
2. you actually put your key in there (not just the placeholder)
3. you installed crewai with pip install crewai python-dotenv

come back if it crashes, we'll fix it 💪

### User
AYO IT WORKED LET'S GOOOO 😭🙏

### AI
LESSS GOOOO! glad it worked! now just:
1. Save your output.txt
2. Make sure prompt-log.md has everything
3. README.md with your reflection
4. Push to GitHub

you got this! lmk if you need anything else

### User
ur the goat fr thank u!!

### AI
anytime! good luck with the grade, you got this 🚀


