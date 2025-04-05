def fix_code(code):
    fixed_code = code.replace("pritn", "print")
    logs = ""
    if "pritn" in code:
        logs += "Found and fixed typo: 'pritn' → 'print'\n"
    return fixed_code, logs
