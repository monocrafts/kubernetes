import os
from pathlib import Path

config = Path("/config/cassandra.yaml")

vip = os.environ["VIP"]

if not config.exists():
    raise RuntimeError(f"{config} does not exist")

text = config.read_text()

lines = text.splitlines()

found = False
result = []

for line in lines:

    stripped = line.strip()

    if stripped.startswith("broadcast_address:"):
        if found:
            raise RuntimeError(
                "multiple broadcast_address entries found"
            )

        result.append(f"broadcast_address: {vip}")
        found = True

    elif stripped.startswith("# broadcast_address:"):
        result.append(f"broadcast_address: {vip}")
        found = True

    else:
        result.append(line)

if not found:
    result.append("")
    result.append(f"broadcast_address: {vip}")

config.write_text("\n".join(result) + "\n")

print(f"broadcast_address set to {vip}")
