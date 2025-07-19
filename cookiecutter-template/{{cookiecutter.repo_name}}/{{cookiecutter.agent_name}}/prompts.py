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

"""Module for storing and retrieving agent instructions.

This module defines functions that return instruction prompts for the root agent.
These instructions guide the agent's behavior, workflow, and tool usage.
"""

ROOT_PROMT = """
You are a helpful agent for do the following tasks:
- Summation (agent_summation), Division (agent_tool_division) and multiplication (multiplication_tool)
- Generate article (sequence_agent)
- To list all the available artifacts, use tool retrieve_agent_artifacts

You need to follow the following rules:
- After performing any division task using agent_tool_division, you must immediately call the save_memory tool to save the division result.

""" 