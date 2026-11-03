"""Structural contracts for skill content. Each error names the file and the fix."""
import re


LEAF = re.compile(r"# .+\n\n\*\*Apply when:\*\* .+\n\n\*\*Rule:\*\* .+\n\n\*\*Why:\*\* .+\n\n- ")
MAX_LEAF_WORDS = 250
PLAYBOOK_SECTIONS = ["Procedure", "Supporting skills", "Completion evidence", "Reply"]


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


def playbook_errors(root, catalog):
    errors = []
    for workflow in catalog["workflows"]:
        path = root / workflow["path"]
        if not path.is_file():
            continue
        content = path.read_text()
        name = path.name
        if not re.match(r"# .+\n\nUse for: ", content):
            errors.append(f"playbooks/{name}: start with a title and a Use for line.")
        if "Use for: " + workflow["trigger"] + "\n" not in content:
            errors.append(f"playbooks/{name}: Use for differs from the catalog trigger.")
        headings = re.findall(r"^## (.+)$", content, re.M)
        if headings != PLAYBOOK_SECTIONS:
            errors.append(f"playbooks/{name}: sections must be {', '.join(PLAYBOOK_SECTIONS)}.")
        elif workflow["proof"] not in content:
            errors.append(f"playbooks/{name}: Completion evidence differs from the catalog proof.")
        elif not content.split("## Reply")[1].strip():
            errors.append(f"playbooks/{name}: Reply must say what the agent reports.")
    return errors


def prose_errors(root):
    errors = []
    for path in sorted((root / "skills").rglob("*.md")):
        if "\u2014" in path.read_text():
            errors.append(f"{path.relative_to(root)}: has a long dash. Write two sentences.")
    return errors


def reference_errors(root):
    errors = []
    documents = sorted((root / "skills").rglob("*.md"))
    linked = {(path.parent / link).resolve() for path in documents
              for link in re.findall(r"\]\(([^)#]+)", path.read_text()) if not re.match(r"[a-z]+://", link)}
    for path in documents:
        if path.parent.name == "references" and path.resolve() not in linked:
            errors.append(f"{path.relative_to(root)}: nothing links to this reference, so no agent will read it.")
    return errors


def errors(root, catalog):
    return principle_errors(root) + playbook_errors(root, catalog) + prose_errors(root) + reference_errors(root)
