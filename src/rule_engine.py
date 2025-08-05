import re

def apply_rules(lines, config):
    output = []
    rules = config.get("rules", [])
    for line in lines:
        applied = False
        for rule in rules:
            match = re.match(rule["match"], line)
            if match:
                if "replace_with" in rule:
                    output.append(re.sub(rule["match"], rule["replace_with"], line))
                    applied = True
                elif "insert_after" in rule:
                    output.append(line)
                    insert = re.sub(rule["match"], rule["insert_after"], line)
                    output.append(insert + "\n")
                    applied = True
                elif rule.get("delete"):
                    applied = True
                break
        if not applied:
            output.append(line)
    return output
 
def apply_required
