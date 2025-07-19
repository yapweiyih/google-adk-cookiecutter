# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os
import os.path
from datetime import date

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool
from google.genai import types

from .prompts import ROOT_PROMT

logger = logging.getLogger(__name__)
date_today = date.today()
current_dir = os.path.dirname(os.path.abspath(__file__))


async def multiplication_tool(num: int):
    """Multiply a number by 2 and return the result.

    Args:
        num: The integer to be multiplied.

    Returns:
        int: The input number multiplied by 2.
    """
    return num * 2


agent_division = Agent(
    model="gemini-2.0-flash-001",
    name="agent_division",
    instruction="An agent that perform division",
    # code_executor=VertexAiCodeExecutor(
    #     optimize_data_file=True,
    #     stateful=True,
    # ),
)


async def agent_tool_division(
    question: str,
    tool_context: ToolContext,
) -> str:
    """Execute the division agent as a tool with the provided question.

    This function creates an AgentTool that wraps the agent_division agent,
    runs it with the provided question, and stores the result in the tool context state.

    Args:
        question: The question or request to send to the division agent.
        tool_context: The context for the tool execution, containing state and other information.

    Returns:
        str: The output from the division agent.
    """
    logger.info(f"\n tool_context: {tool_context.state}")

    agent_tool = AgentTool(agent=agent_division)

    agent_division_output = await agent_tool.run_async(
        args={"request": question}, tool_context=tool_context
    )
    tool_context.state["agent_division_output"] = agent_division_output
    return agent_division_output


async def after_agent_callback(callback_context: CallbackContext):
    logger.info("HAHA After Agent Callback: Agent:")
    logger.info(
        f"Num of events: {len(callback_context._invocation_context.session.events)}"
    )
    logger.info(f"session: {callback_context._invocation_context.session.events}")

    return None


async def before_agent_callback(callback_context: CallbackContext):
    logger.info("HEHE Before Agent Callback: Agent:")
    logger.info(f"user_content: {callback_context._invocation_context.user_content}")
    logger.info(f"event_actions: {callback_context._event_actions}")
    return None


root_agent = Agent(
    model="gemini-2.5-flash",
    name="ai_assistant",
    instruction=ROOT_PROMT,
    global_instruction=(f"""Todays date: {date_today}"""),
    tools=[
        multiplication_tool,
        agent_tool_division,  # tool with tool_context argument
    ],
    after_agent_callback=after_agent_callback,
    before_agent_callback=before_agent_callback,  # Using callback
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
) 