from rapidfuzz import fuzz
import bisect
from mimir.util.packages import get_package_json
from math import tanh
from mimir.util.output import debug, title, end

def main(args, config):
    search_string = args.search_string
    packages = get_package_json()
    top_packages = search_packages(search_string, packages, limit=args.limit, min_score=args.min_score)
    title_txt = "Best Matches"
    title(title_txt)
    for package in top_packages:
        score = round(package[1])
        print(f"({score}) " + package[0])
    end(title_txt)


def search_packages(search_string, packages, limit=10, min_score=40):
    info("Searching for best matches")
    search_string = search_string.lower()
    matches =  []
    for package in packages:
        package_name = package.lower()
        package = packages[package]

        tags = list(map(lambda t: t.lower(), package["tags"]))

        score_name = fuzz.token_set_ratio(search_string, package_name)
        debug(f"==== Score - {package_name} ====")
        debug(f"{score_name=}")
        if score_name >= 85:
            bisect.insort(matches, (package_name,score_name), key=lambda x: -x[1])
            continue

        count = 0
        for tag in tags:
            score_tag = fuzz.token_set_ratio(tag, search_string)
            debug(f"{tag} {score_tag}")
            if score_tag >= 45:
                count += 1
        score_tag = tag_score(count, len(tags))
        debug(f"{score_tag=} {tags=}")
        score = max(score_tag, score_name)
        if score < min_score:
            continue
        bisect.insort(matches, (package_name,score), key=lambda x: -x[1])

    if len(matches) > limit:
        return matches[:limit]
    return matches


def tag_score(matched_count, tag_count):
    x = min(matched_count, 5) / tag_count
    score = tanh(2* x) * 100
    
    return score