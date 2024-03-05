def main(lines):
    seeds = [int(x) for x in lines[0].split(":")[1].strip().split()]
    i = 2
    while i < len(lines) - 1:
        mapped = []
        mapping = []
        while i < len(lines) - 1 and lines[i] != "\n":
            mapping.append(lines[i])
            i += 1
        i += 1
        for seed in seeds:
            added = False
            for line in mapping[1:]:
                destination, source, range_len = [int(x) for x in line.split()]
                if source <= seed <= source + range_len:
                    mapped.append(destination + seed - source)
                    added = True
                    break
            if not added:
                mapped.append(seed)
            seeds = mapped
    print(f"Part 1: {min(seeds)}")
    pass


def main2(lines):
    seeds = iter([int(x) for x in lines[0].split(":")[1].strip().split()])
    seed_pairs = []
    for seed in seeds:
        seed_pairs.append(range(seed, seed + next(seeds)))
    print(seed_pairs)
    i = 2
    not_checked = seed_pairs

    while i < len(lines) - 1:
        mapping = []
        while i < len(lines) - 1 and lines[i] != "\n":
            mapping.append(lines[i])
            i += 1
        i += 1

        mapped = []
        print(mapping[0])
        for line in mapping[1:]:
            destination, source, range_len = [int(x) for x in line.split()]
            offset = destination - source
            map_range = range(source, source + range_len)
            not_mapped = []
            for seed in not_checked:
                if seed.start < map_range.stop and seed.stop >= map_range.start:
                    overlap = range(
                        max(seed.start, map_range.start), min(seed.stop, map_range.stop)
                    )
                else:
                    overlap = range(seed.start, seed.start)

                overlapped = range(seed.start, overlap.start)
                if overlapped.stop > overlapped.start:
                    not_mapped.append(overlapped)
                if overlap.stop > overlap.start:
                    mapped.append(range(overlap.start + offset, overlap.stop + offset))

                overlapped = range(overlap.stop, seed.stop)
                if overlapped.stop > overlapped.start:
                    not_mapped.append(overlapped)
            not_checked = not_mapped
        not_checked = mapped + not_checked
    print(min([x.start for x in not_checked]))
    pass


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    main(lines)
    main2(lines)
