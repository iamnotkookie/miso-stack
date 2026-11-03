# MisoStack development

Read `plugins/miso-stack/skills/miso/SKILL.md` for engineering work on this stack. Follow the current request for commits. Remotes and publication require authorization. `package.json` owns the version; `scripts/check_repository.py` rejects a manifest that differs.

Use the shared source tree. Do not vendor third-party skill code. Keep factual qualification separate from documentation claims. Run `python3 plugins/miso-stack/scripts/miso.py check`, `python3 -m unittest discover -s tests`, and `python3 scripts/check_repository.py` after relevant changes.

Use temporary sandbox folders for agent evaluations. Keep `evidence/` local and ignored by Git. Do not publish traces that contain private configuration or credentials. Record remaining host limitations honestly.
