#!/usr/bin/env python3
"""Regenerate landing-i18n.js from the per-language i18n/landing.<code>.json files."""
import json, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I18N = os.path.join(ROOT, 'i18n')
out = {}
en = json.load(open(os.path.join(I18N, 'landing.en.json'), encoding='utf-8'))
out['en'] = en
for path in sorted(glob.glob(os.path.join(I18N, 'landing.*.json'))):
    code = os.path.basename(path)[len('landing.'):-len('.json')]
    if code == 'en':
        continue
    d = json.load(open(path, encoding='utf-8'))
    missing = [k for k in en if k not in d]
    if missing:
        print(f"  WARN {code}: missing {len(missing)} keys -> {missing[:3]}...")
    out[code] = d
body = ",\n".join(
    f'  {json.dumps(code, ensure_ascii=False)}: {json.dumps(out[code], ensure_ascii=False, separators=(",", ":"))}'
    for code in (['en'] + sorted(c for c in out if c != 'en'))
)
js = ("// Auto-generated landing-page translation dictionary.\n"
      "// Source: i18n/landing.<code>.json (regenerate via tools/build-landing-i18n.py).\n"
      "window.LANDING_I18N = {\n" + body + "\n};\n")
open(os.path.join(ROOT, 'landing-i18n.js'), 'w', encoding='utf-8').write(js)
print(f"Wrote landing-i18n.js with {len(out)} languages ({len(en)} keys each).")
