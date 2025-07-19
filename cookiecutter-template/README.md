# Cookiecutter Fairprice Template

This is a Cookiecutter template to generate a repo with the following structure:

```
{{cookiecutter.repo_name}}/
├── agents
│   └── {{cookiecutter.agent_name}}
│       ├── {{cookiecutter.agent_name}}
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── prompts.py
│       │   └── .env.example
│       └── README.md
├── pyproject.toml
└── uv.lock
```

## Usage

```bash
cookiecutter path/to/cookiecutter-fairprice
# OR
cookiecutter https://github.com/weiyih/202507-adk-cookiecutter.git --directory cookiecutter-template
```

You will be prompted for `repo_name` and `agent_name`. 