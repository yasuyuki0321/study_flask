# python_devcontainer

## Usage

### clone

```sh
git clone https://github.com/yasuyuki0321/python_devcontainer.git
```

### change repository

```sh
git remote set-url origin {new-url}
```

### check

```sh
git remote -v
```

### initialize the repository

```sh
git remote -v

rm -rf .git
git init
git add .
git commit -m "初期登録"
git remote add origin {remote-url}

git push -f origin master
```
