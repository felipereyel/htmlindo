from .__ctx__ import Context


def run(ctx: Context):
    name = ctx.read("Name", placeholder="Enter your name")
    print(f"Name: {name}")

    age = ctx.read("Age", placeholder="Enter your age")
    print(f"Age: {age}")

    ctx.display(f"Hello {name}, you are {age} years old!")
