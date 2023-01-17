بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
# quran_server
Server API used for [Bless](https://github.com/bal-sm/bless) app (and other apps) / Standalone Qur'an (WORK IN PROGRESS)

## How-to

### Install Python

[Download](https://www.python.org/downloads/)

### Install pipx (Optional)
Run this command:
```bash
python3 -m pip install --user pipx
```

### Ensure path (after installing pipx)
Don't forget to run this command after installing pipx:
```bash
python3 -m pipx ensurepath
```

### Install Poetry
If you use pipx, you can just run this command:
```bash
python3 -m pipx install poetry
```

Or:
[Installation Docs](https://python-poetry.org/docs/#installation)

### Have a copy of this repository
You can use Git (and GitHub) tutorial linked below for conscise beginner-friendly tutorials

### Install dependencies with Poetry
Run this command on the root folder of the project:
```bash
poetry install --with=dev
```

### Activate the virtual environment
Run this command on the root folder of the project:
```bash
poetry shell
```

### Run the server
Run this command on the root folder of the project:
```bash
python3 manage.py runserver
```

### Develop using Visual Studio Code
1. Rename `quran_server.code-workspace.dist` located on the root folder of the project to `quran_server.code-workspace`
2. Open the `quran_server.code-workspace`
3. Install
    these extensions:

    [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

    [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

    [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) (Prettier doesn't work well for Django HTML yet, so it only be used for css only)

## Source
For An-Nas: [Qur'an Kemenag](https://quran.kemenag.go.id/)

## Please
### For commit message
A written example:
Created \`AUTHORS\`

So, it will be seen like this:
Created `AUTHORS`

Sorry, if I also did many inconsistencies :(
#### Use verb 3
"Created"
#### Please add "`" charater to the start and the end of an object
"\`AUTHORS\`"

#### See these tutorials

[GIT & GITHUB by Sandhika Galih (Indonesian)](https://youtube.com/playlist?list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf)

[Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)

[Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4)

[Django For Everybody - Full Python University Course](https://www.youtube.com/watch?v=o0XbHvKxw7Y)

### Dear Authors
Don't forget to add yourself in `AUTHORS` file, if you contributed to this project (and haven't done that yet)

### Discuss with these persons
For more information:

[CallMeKevin](callmekevinbusiness@gmail.com)

[Django Forum](https://forum.djangoproject.com/t/lets-contribute-to-my-quran-server-project/18086)
