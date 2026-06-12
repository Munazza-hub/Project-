import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def planner_agent(user_input):
    time.sleep(2)
    return model.generate_content(
        "You are a planning agent.\nBreak into steps.\n\nUser: " + user_input
    ).text


def research_agent(plan):
    time.sleep(2)
    return model.generate_content(
        "You are a research agent.\nGive insights.\n\nPlan: " + plan
    ).text


def critic_agent(research):
    time.sleep(2)
    return model.generate_content(
        "You are a critic agent.\nFind mistakes.\n\nResearch: " + research
    ).text


def writer_agent(plan, research, critique):
    time.sleep(2)
    return model.generate_content(
        "Final writer agent.\nCombine everything:\n\n"
        f"Plan:\n{plan}\n\nResearch:\n{research}\n\nCritique:\n{critique}"
    ).text