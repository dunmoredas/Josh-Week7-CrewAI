import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# Load environment variables
load_dotenv()

# Initialize LLM
llm = LLM(
    model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
    base_url=os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com"),
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

# Agent 1: Market Researcher
researcher = Agent(
    role="Market Research Specialist",
    goal="Conduct comprehensive market research on the specified business topic, "
         "identifying key trends, market size, competitors, and growth opportunities",
    backstory="""You are a senior market researcher with 15 years of experience 
    in technology and business analysis. You've worked with Fortune 500 companies 
    and startups alike, helping them understand market dynamics. Your specialty is 
    identifying emerging trends before they become mainstream. You're known for 
    your meticulous attention to data accuracy and ability to synthesize complex 
    market information into actionable insights.""",
    llm=llm,
    verbose=True
)

# Agent 2: Business Analyst
analyst = Agent(
    role="Business Strategy Analyst",
    goal="Analyze market research data to identify business opportunities, "
         "risks, and strategic recommendations for market entry or expansion",
    backstory="""You are a strategic business analyst with expertise in market 
    entry strategies and business model innovation. You've helped over 50 companies 
    successfully enter new markets. Your analytical approach combines traditional 
    business frameworks (SWOT, Porter's Five Forces) with modern agile methodologies. 
    You're known for translating complex data into clear, actionable business strategies.""",
    llm=llm,
    verbose=True
)

# Agent 3: Report Writer
writer = Agent(
    role="Executive Report Writer",
    goal="Transform research findings and strategic analysis into a polished, "
         "professional business report suitable for C-level executives",
    backstory="""You are a professional business writer who specializes in creating 
    executive-level reports and presentations. With a background in business journalism 
    and corporate communications, you excel at making complex information accessible 
    and compelling. Your reports are known for being concise yet comprehensive, with 
    clear structure and actionable recommendations. You understand what executives 
    need to make informed decisions.""",
    llm=llm,
    verbose=True
)

# Task 1: Research Phase
task1 = Task(
    description="""Conduct thorough market research on {topic}. 
    
    Your research should include:
    1. Current market size and projected growth (next 3-5 years)
    2. Key market trends and drivers
    3. Major competitors and their market share
    4. Customer demographics and behavior patterns
    5. Regulatory environment and potential barriers
    6. Emerging opportunities and threats
    
    Use reliable data sources and provide specific numbers where possible.""",
    expected_output="""A comprehensive market research report containing:
    - Executive summary of key findings
    - Detailed market analysis with statistics
    - Competitor landscape overview
    - SWOT analysis of the market opportunity
    - Citations for key data points (can be estimated if real data unavailable)""",
    agent=researcher
)

# Task 2: Analysis Phase
task2 = Task(
    description="""Based on the market research provided, develop a strategic analysis.
    
    Your analysis should include:
    1. Market entry/expansion feasibility assessment
    2. Identification of key success factors
    3. Risk assessment and mitigation strategies
    4. Recommended business model or approach
    5. Required resources and capabilities
    6. Financial projections and ROI estimates
    
    Focus on actionable insights that executives can use for decision-making.""",
    expected_output="""A detailed strategic analysis document containing:
    - Feasibility assessment with justification
    - Strategic recommendations (short-term and long-term)
    - Risk analysis with mitigation strategies
    - Resource requirements and timeline
    - Financial projections (conservative, moderate, optimistic scenarios)""",
    agent=analyst,
    context=[task1]
)

# Task 3: Reporting Phase
task3 = Task(
    description="""Create a polished executive report that synthesizes the market research 
    and strategic analysis into a professional document.
    
    The report should:
    1. Start with a compelling executive summary
    2. Present key findings in a logical flow
    3. Include visual elements (described in text)
    4. Highlight critical insights and recommendations
    5. End with a clear call to action
    6. Maintain professional tone suitable for C-level executives
    
    Ensure the report is concise (3-5 pages equivalent) but comprehensive enough to 
    support strategic decision-making.""",
    expected_output="""A professional executive report with:
    - Title page with topic and date
    - Executive summary (1 page)
    - Market opportunity analysis
    - Strategic recommendations
    - Implementation roadmap
    - Risk considerations
    - Next steps and call to action
    - Appendix with key data sources""",
    agent=writer,
    context=[task1, task2]
)

# Create and execute the crew
crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    verbose=True
)

# Define the business topic
topic = "AI-Powered Customer Service Solutions in North America"

# Execute the crew
print("\n" + "="*80)
print(f"Starting CrewAI execution for: {topic}")
print("="*80 + "\n")

result = crew.kickoff(inputs={"topic": topic})

print("\n" + "="*80)
print("FINAL REPORT:")
print("="*80)
print(result)
print("\n" + "="*80)