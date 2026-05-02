from pathlib import Path
p = Path('bmtc-pass-app-code.html')
text = p.read_text(encoding='utf-8')
Path('bmtc-pass-app-code.html').write_text(text, encoding='utf-8')
print('written')