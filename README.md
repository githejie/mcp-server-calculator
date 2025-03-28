# Calculator MCP Server
[![smithery badge](https://smithery.ai/badge/@githejie/mcp-server-calculator)](https://smithery.ai/server/@githejie/mcp-server-calculator)

A Model Context Protocol server for calculating. This server enables LLMs to use calculator for precise numerical calculations.

### Available Tools

- `calculate` - Calculates/evaluates the given expression.
  - `expression` (string, required): Expression to be calculated

## Installation

### Installing via Smithery

To install Calculator MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@githejie/mcp-server-calculator):

```bash
npx -y @smithery/cli install @githejie/mcp-server-calculator --client claude
```

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *mcp-server-calculator*.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Using PIP

Alternatively you can install `mcp-server-calculator` via pip:

```bash
pip install mcp-server-calculator
```

After installation, you can run it as a script using:

```bash
python -m mcp_server_calculator
```

## Configuration

### Using uv (recommended)

Add this to your MCP client settings:

```json
"mcpServers": {
  "calculator": {
    "command": "uvx",
    "args": ["mcp-server-calculator"]
  }
}
```

### Using PIP

Alternatively add this to your MCP client settings:

```json
"mcpServers": {
  "calculator": {
    "command": "python",
    "args": ["-m", "mcp_server_calculator"]
  }
}
```

## License

mcp-server-calculator is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
