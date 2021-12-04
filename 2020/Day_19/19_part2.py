import itertools

def parse_input(txt):
    raw_rules, messages = (x.splitlines() for x in txt.split("\n\n"))
    rules = {}

    for rule in raw_rules:
        i, v = rule.split(":")
        i = int(i)
        v = v.strip().replace("\"", "").split(" | ")
        if v[0] in "ab":
            rules[i] = v[0]
        else:
            rules[i] = [[int(x) for x in v.split()] for v in v]
        #print(i, rules[i])

    return rules, messages

def resolve_rules(rules, cache, i=0):
    #if current rule (as determined by i) has been fully resolved, retreive from cache
    if i in cache:
        return cache[i]
    
    
    rule = rules[i]
    #if the rule is just a string with no other rules, return the string
    if isinstance(rule, str):
        cache[i] = rule
        return rule

    out = []

    for subrule in rule:
        temp = [resolve_rules(rules, cache, next_i) for next_i in subrule]
        #print([x for x in itertools.product(*temp)])
        out.extend("".join(x) for x in itertools.product(*temp))
        #print(i, subrule, out)
    cache[i] = out

    return out


def part_1(rules, messages):
    valid_messages = set(resolve_rules(rules, {}))
    return sum(message in valid_messages for message in messages)

def part_2(rules, messages):
    # For an explanation see the bottom of this script.

    # 8: 42 | 42 8
    rules[8] = [[42], [42, 8]]
    # 11: 42 31 | 42 11 31
    rules[11] = [[42, 31], [42, 11, 31]]

    rule_cache = {}  # share the cache for both searches
    r_31 = set(resolve_rules(rules, rule_cache, 31))
    r_42 = set(resolve_rules(rules, rule_cache, 42))
    # print(r_31)
    # print(r_42)
    len_31 = {len(x) for x in r_31}
    len_42 = {len(x) for x in r_42}
    len_both = len_31 | len_42
    assert len(len_both) == 1
    word_len = len_both.pop()

    sum_valid = 0
    for m in messages:
        words = [m[0+i:word_len+i] for i in range(0, len(m), word_len)]
        n_words = len(words)

        n_31 = 0
        for word in reversed(words):
            if word in r_31:
                n_31 += 1
            else:
                break
        if 0 < n_31 < n_words/2 and all(word in r_42 for word in words[:-n_31]):
            sum_valid += 1

    return sum_valid

f = open("C:/Users/mattr/Documents/Advent-Coding/Day_19/19_input.txt", "r")
input = parse_input(f.read())
print(part_1(*input))
print(part_2(*input))