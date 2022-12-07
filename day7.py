with open("day7.txt") as f:
    data = f.read()

directories = {}
parent = []
for line in data.splitlines():
    if line.startswith("$"):
        command, *args = line[2:].split()
        if command == "cd":
            if args[0] == "..":
                parent.pop()
                continue
            parent.append(args[0])
            if not args[0] in directories:
                directories["/".join(parent)] = {
                    "type": "directory",
                    "parent": parent[:-1],
                    "size": 0,
                }
    else:
        size, name = line.split()
        if size == "dir":
            continue
        size = int(size)
        directories["/".join(parent + [name])] = {
            "type": "file",
            "parent": parent,
            "size": size,
        }
        for i in range(len(parent)):
            directories["/".join(parent[: i + 1])]["size"] += size

# Part 1
total_size = 0
for info in directories.values():
    if info["size"] <= 100000 and info["type"] == "directory":
        total_size += info["size"]

print(total_size)

# Part 2
space_used = directories["/"]["size"]
space_available = 70000000
space_needed = 30000000 - (space_available - space_used)
size_to_delete = space_used
for info in directories.values():
    if (
        info["size"] >= space_needed
        and info["size"] < size_to_delete
        and info["type"] == "directory"
    ):
        size_to_delete = info["size"]

print(size_to_delete)
