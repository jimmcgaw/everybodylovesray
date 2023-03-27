import ray

items = [
    {"name": f"Item {x}", "data": x}
    for x
    in range(10000)
]
dataset = ray.data.from_items(items)
dataset.show(10)

pipe = dataset.window()
result = pipe.map(
    lambda x: x["data"] ** 2
).filter(
    lambda x: x % 2 == 0
).flat_map(
    lambda x: [x, x**3]
)
result.show()