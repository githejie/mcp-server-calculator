import ast
import operator
from mcp.server.fastmcp import FastMCP

def evaluate(expression: str) -> str:
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
    }

    def eval_expr(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = eval_expr(node.left)
            right = eval_expr(node.right)
            if type(node.op) in allowed_operators:
                return allowed_operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -eval_expr(node.operand)
        raise ValueError("Unsupported operation")

    parsed_expr = ast.parse(expression, mode='eval')
    result = eval_expr(parsed_expr.body)
    return str(result)

mcp = FastMCP("calculator")

@mcp.tool()
async def calculate(expression: str) -> str:
    """Calculates/evaluates the given expression."""
    return evaluate(expression)

def main():
    mcp.run()
