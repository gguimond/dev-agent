This file is a merged representation of a subset of the codebase, containing files not matching ignore patterns, combined into a single document by Repomix.
The content has been processed where comments have been removed, line numbers have been added.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching these patterns are excluded: **/node_modules/**
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Code comments have been removed from supported file types
- Line numbers have been added to the beginning of each line
- Files are sorted by Git change count (files with more changes are at the bottom)

## Additional Info

# Directory Structure
```
.gitignore
.tool-versions
package.json
README.md
repomix.config.json
requirements.txt
utils.py
```

# Files

## File: .tool-versions
```
1: yarn 1.22.22
```

## File: package.json
```json
1: {
2:   "dependencies": {
3:     "repomix": "^0.3.0"
4:   }
5: }
```

## File: repomix.config.json
```json
 1: {
 2:   "output": {
 3:     "style": "markdown",
 4:     "filePath": "custom-output.md",
 5:     "removeComments": true,
 6:     "showLineNumbers": true,
 7:     "topFilesLength": 10
 8:   },
 9:   "ignore": {
10:     "customPatterns": ["**/node_modules/**"]
11:   }
12: }
```

## File: requirements.txt
```
1: pocketflow>=0.0.1
2: openai>=1.0.0
```

## File: utils.py
```python
 1: from openai import OpenAI
 2: import os
 3: 
 4: llm_api_key = os.environ.get("LITELLM_API_KEY")
 5: llm_api_base = "https://llmproxy.ai.orange"
 6: 
 7: def call_llm(prompt):
 8:     client = OpenAI(
 9:         api_key=llm_api_key,
10:         base_url=llm_api_base
11:     )
12:     response = client.chat.completions.create(
13:         model="openai/gpt-4o-mini",
14:         messages = [
15:             {"role": "user", "content": prompt},
16:         ]
17:     )
18:     return response.choices[0].message.content
19: 
20: def call_repomix(prompt):
21:     os.system('node ./node_modules/repomix/bin/repomix.cjs ' + '.')
22: 
23: def read_file(path):
24:     f=open(path)
25:     s=f.read()
26:     f.close()
27:     return s
28: 
29: if __name__ == "__main__":
30:     print("## Testing call_llm")
31:     prompt = "In a few words, what is the meaning of life?"
32:     print(f"## Prompt: {prompt}")
33:     response = call_llm(prompt)
34:     print(f"## Response: {response}")
35: 
36:     print("## Testing call_repomix")
37:     call_repomix(prompt)
38: 
39:     print("## Testing read_file")
40:     print(read_file('custom-output.md'))
```

## File: .gitignore
```
  1: # Byte-compiled / optimized / DLL files
  2: __pycache__/
  3: *.py[cod]
  4: *$py.class
  5: 
  6: # C extensions
  7: *.so
  8: 
  9: # Distribution / packaging
 10: .Python
 11: build/
 12: develop-eggs/
 13: dist/
 14: downloads/
 15: eggs/
 16: .eggs/
 17: lib/
 18: lib64/
 19: parts/
 20: sdist/
 21: var/
 22: wheels/
 23: share/python-wheels/
 24: *.egg-info/
 25: .installed.cfg
 26: *.egg
 27: MANIFEST
 28: 
 29: # PyInstaller
 30: #  Usually these files are written by a python script from a template
 31: #  before PyInstaller builds the exe, so as to inject date/other infos into it.
 32: *.manifest
 33: *.spec
 34: 
 35: # Installer logs
 36: pip-log.txt
 37: pip-delete-this-directory.txt
 38: 
 39: # Unit test / coverage reports
 40: htmlcov/
 41: .tox/
 42: .nox/
 43: .coverage
 44: .coverage.*
 45: .cache
 46: nosetests.xml
 47: coverage.xml
 48: *.cover
 49: *.py,cover
 50: .hypothesis/
 51: .pytest_cache/
 52: cover/
 53: 
 54: # Translations
 55: *.mo
 56: *.pot
 57: 
 58: # Django stuff:
 59: *.log
 60: local_settings.py
 61: db.sqlite3
 62: db.sqlite3-journal
 63: 
 64: # Flask stuff:
 65: instance/
 66: .webassets-cache
 67: 
 68: # Scrapy stuff:
 69: .scrapy
 70: 
 71: # Sphinx documentation
 72: docs/_build/
 73: 
 74: # PyBuilder
 75: .pybuilder/
 76: target/
 77: 
 78: # Jupyter Notebook
 79: .ipynb_checkpoints
 80: 
 81: # IPython
 82: profile_default/
 83: ipython_config.py
 84: 
 85: # pyenv
 86: #   For a library or package, you might want to ignore these files since the code is
 87: #   intended to run in multiple environments; otherwise, check them in:
 88: # .python-version
 89: 
 90: # pipenv
 91: #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
 92: #   However, in case of collaboration, if having platform-specific dependencies or dependencies
 93: #   having no cross-platform support, pipenv may install dependencies that don't work, or not
 94: #   install all needed dependencies.
 95: #Pipfile.lock
 96: 
 97: # UV
 98: #   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
 99: #   This is especially recommended for binary packages to ensure reproducibility, and is more
100: #   commonly ignored for libraries.
101: #uv.lock
102: 
103: # poetry
104: #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
105: #   This is especially recommended for binary packages to ensure reproducibility, and is more
106: #   commonly ignored for libraries.
107: #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
108: #poetry.lock
109: 
110: # pdm
111: #   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
112: #pdm.lock
113: #   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
114: #   in version control.
115: #   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
116: .pdm.toml
117: .pdm-python
118: .pdm-build/
119: 
120: # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
121: __pypackages__/
122: 
123: # Celery stuff
124: celerybeat-schedule
125: celerybeat.pid
126: 
127: # SageMath parsed files
128: *.sage.py
129: 
130: # Environments
131: .env
132: .venv
133: env/
134: venv/
135: ENV/
136: env.bak/
137: venv.bak/
138: 
139: # Spyder project settings
140: .spyderproject
141: .spyproject
142: 
143: # Rope project settings
144: .ropeproject
145: 
146: # mkdocs documentation
147: /site
148: 
149: # mypy
150: .mypy_cache/
151: .dmypy.json
152: dmypy.json
153: 
154: # Pyre type checker
155: .pyre/
156: 
157: # pytype static type analyzer
158: .pytype/
159: 
160: # Cython debug symbols
161: cython_debug/
162: 
163: # PyCharm
164: #  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
165: #  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
166: #  and can be added to the global gitignore or merged into this file.  For a more nuclear
167: #  option (not recommended) you can uncomment the following to ignore the entire idea folder.
168: #.idea/
169: 
170: # Ruff stuff:
171: .ruff_cache/
172: 
173: # PyPI configuration file
174: .pypirc
175: 
176: ##########################npm
177: 
178: node_modules
179: /dist
180: /coverage
181: # Log files
182: npm-debug.log*
183: yarn-debug.log*
184: yarn-error.log*
185: pnpm-debug.log*
186: 
187: #env
188: .env
189: 
190: # Editor directories and files
191: .idea
192: .vscode
193: *.suo
194: *.ntvs*
195: *.njsproj
196: *.sln
197: *.sw?
198: .nvmrc
```

## File: README.md
```markdown
1: # dev-agent
```
