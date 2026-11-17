# Nutmeg – how to update

This repo publishes an encrypted, read-only copy of a workload tracker to GitHub Pages.
The plaintext data is never stored here. The master data lives in the owner's private
Claude artifact (file `data/tracker.json`); its link is in the owner's project instructions.

## Rebuild after a check-in
1. Read `data/tracker.json` from the private artifact and apply the agreed changes.
2. Put the data at `<work>/data/tracker.json`, copy `tools/template.html` and `tools/build.py`
   to `<work>/src/`, and `keys/*` to `<work>/keys/`.
3. `python3 <work>/src/build.py <work>` writes `dist/private/index.html` (plain) and
   `dist/public/index.html` (encrypted with `keys/public.pem`; no password needed).
4. Republish the private artifact (page + `data/tracker.json`), then copy
   `dist/public/index.html` to `index.html` here, commit and push to `main`.
5. Check the public file contains no plaintext project names before pushing.

## Data shape (tracker.json)
- `meta.updated` – date of the last check-in.
- `week` – `label`, `days[{date, items[], note}]`, `priorities{must,should,iftime}[{text,pid,done}]`, `ellis[{text,pid,done}]`.
- `projects[]` – `id, theme, title, detail, status, rag, flag, owner, due, next, why, decision, updates[{date,status,text}]` (newest first).
- `wins[]` – `date (YYYY-MM or YYYY-MM-DD), title, impact, evidence|null, who (Ella|Ellis|Team), pid`.

## Rules
- RAG ratings change only when the owner says so.
- Never tick tasks for the owner from guesswork: completions come from her Friday OneNote screenshot or what she says.
- Unticked OneNote items carry forward into next week's priorities.
- Every completed milestone is a candidate win: log impact, and ask for evidence when missing.
