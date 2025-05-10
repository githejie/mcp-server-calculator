import ast
import operator
import math
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
    allowed_names = {
        k: getattr(math, k)
        for k in dir(math)
        if not k.startswith("__")
    }
    allowed_names.update({
        "pi": math.pi,
        "e": math.e,
    })

    def eval_expr(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Name):
            if node.id in allowed_names:
                return allowed_names[node.id]
            raise ValueError(f"Unknown identifier: {node.id}")
        elif isinstance(node, ast.BinOp):
            left = eval_expr(node.left)
            right = eval_expr(node.right)
            if type(node.op) in allowed_operators:
                return allowed_operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -eval_expr(node.operand)
        elif isinstance(node, ast.Call):
            func = eval_expr(node.func)
            args = [eval_expr(arg) for arg in node.args]
            return func(*args)
        raise ValueError(f"Unsupported operation: {ast.dump(node)}")

    expression = expression.replace('^', '**').replace('×', '*').replace('÷', '/')
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
