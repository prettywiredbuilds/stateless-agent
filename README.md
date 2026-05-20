# Stateless Agent

A basic Python agent built with the Anthropic SDK that processes each user message independently, with no conversation history retained between turns. Each message sent to the model is treated as a fresh conversation — the agent has no memory of prior exchanges.

## Prerequisites

- Python 3.8+
- An [Anthropic API key](https://console.anthropic.com/)
- The `anthropic` Python package

Install the required package:

```bash
pip install anthropic
```

Set your API key as an environment variable:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Run the Sample

```bash
python chat.py
```

Once running, type a message and press Enter to get a response. Type `quit` to exit.

## Issues & Questions

If you run into any problems or have questions, please [file an issue](../../issues).
