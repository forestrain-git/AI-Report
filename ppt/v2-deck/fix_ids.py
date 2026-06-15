import re

filepath = r'D:\Projects\AI-Report\ppt\v2-deck\AI宣讲-v2.1-guizang.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find ALL section.slide elements with id attributes
pattern = r'<section\s+class="slide[^"]*"\s+id="([^"]+)"'
matches = list(re.finditer(pattern, content))
print(f'Found {len(matches)} slide sections')

# Renumber non-TOC slides sequentially
counter = 1
for m in matches:
    old_id = m.group(1)
    if 'slide-toc' in old_id:
        continue
    new_id = f'slide-{counter}'
    if old_id != new_id:
        # Replace the id in the section tag
        old_tag = m.group(0)
        new_tag = old_tag.replace(f'id="{old_id}"', f'id="{new_id}"')
        content = content.replace(old_tag, new_tag, 1)
        print(f'  {old_id} -> {new_id}')
    counter += 1

content_slides = counter - 1
print(f'Total content slides: {content_slides}')

# Update goto dialog max and placeholder
content = re.sub(r'max="\d+"', f'max="{content_slides}"', content, count=1)
content = re.sub(r'placeholder="\d+-\d+"', f'placeholder="1-{content_slides}"', content, count=1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done! All IDs renumbered 1-{content_slides}.')
