"""Structural contracts for skill content. Each error names the file and the fix."""
import re


LEAF = re.compile(r"# .+\n\n\*\*Apply when:\*\* .+\n\n\*\*Rule:\*\* .+\n\n\*\*Why:\*\* .+\n\n- ")
MAX_LEAF_WORDS = 250


def principle_errors(root):
    errors = []
    references = root / "skills/miso/references"
    index = references / "principles.md"
    entry = root / "skills/miso/SKILL.md"
    leaves = {path.name: path for path in (references / "principles").glob("*.md")}
    linked = re.findall(r"\]\(principles/([^)#]+)\)", index.read_text())
    for name in sorted(set(linked)):
        if linked.count(name) > 1:
            errors.append(f"principles.md: {name} is listed twice. Keep one row for each leaf.")
    for name in sorted(leaves.keys() - set(linked)):
        errors.append(f"principles.md: {name} has no row. Add the moment it applies.")
    for name, path in sorted(leaves.items()):
        content = path.read_text()
        if not LEAF.match(content):
            errors.append(f"principles/{name}: use a title, Apply when, Rule, Why, then action bullets.")
        if len(content.split()) > MAX_LEAF_WORDS:
            errors.append(f"principles/{name}: more than {MAX_LEAF_WORDS} words. A leaf is one idea.")
    for path in sorted((root / "skills").rglob("*.md")):
        if path in (entry, index):
            continue
        for link in re.findall(r"\]\(([^)#]+)", path.read_text()):
            if not re.match(r"[a-z]+://", link) and (path.parent / link).resolve() == index.resolve():
                errors.append(f"{path.relative_to(root)}: cites the principles index. Link the leaf so the citation is checked.")
    return errors


def errors(root):
    return principle_errors(root)
