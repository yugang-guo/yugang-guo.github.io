# git config

```shell
# 查看git用户信息
$ git config user.name
$ git config user.email

# 配置git用户信息
$ git config –-global user.name "<用户名>"
$ git config –-global user.email "<邮箱地址>"
```

# git init

```shell
# 创建一个空的git仓库或重新初始化一个现有仓库。

$ git init [仓库名]
```

# git clone

```shell
# 默认在当前目录下clone主分支
$ git clone <远程仓库>

# 指定本地目录、clone的其他分支
$ git clone <远程仓库> [-b <分支名>] [<本地目录>]
```

# git branch

```shell
# 列出本地的所有分支，当前所在分支以 "*" 标出
$ git branch

# 列出本地的所有分支并显示最后一次提交，当前所在分支以 "*" 标出
$ git branch -v

# 创建新分支，新的分支基于上一次提交建立
$ git branch <分支名>

# 修改分支名称
# 如果不指定原分支名称则为当前所在分支
$ git branch -m [<原分支名称>] <新的分支名称>
# 强制修改分支名称
$ git branch -M [<原分支名称>] <新的分支名称>

# 删除指定的本地分支
$ git branch -d <分支名称>
# 强制删除指定的本地分支
$ git branch -D <分支名称>
```

# git checkout

```shell
# 切换到已存在的指定分支
$ git checkout <分支名称>

# 新建分支并切换该分支（等同于 "git branch" 和 "git checkout" 两个命令合并）
$ git checkout -b <分支名称>
```

# git add

```shell
# 添加文件到暂存区
$ git add <文件名>

# 添加所有修改、已删除的文件到暂存区中
$ git add -u [<文件路径>]
$ git add --update [<文件路径>]

# 添加所有修改、已删除、新增的文件到暂存区中，省略 <文件路径> 即为当前目录
$ git add -A [<文件路径>]
$ git add --all [<文件路径>]
```

# git commit

```shell
# 使用git commit前需使用git add命令将文件添加到暂存区

# 将暂存区的文件提交到本地仓库，调用文件编辑器输入描述信息
$ git commit

# 将暂存区的文件提交到本地仓库，并添加描述信息
$ git commit -m "[描述信息]"
```

```shell
# 不需使用git add命令将文件添加到暂存区

# 把所有修改、已删除的文件提交到本地仓库中，等同于先调用了 "git add -u"（不包括新增的文件)
$ git commit -a -m "[描述信息]"
```

# git pull

```shell
# 从远程仓库获取最新版本并合并到本地仓库（默认主分支）
$ git pull

# 从远程仓库的分支获取最新版本并合并到本地仓库
$ git pull <远程仓库> <远程分支>
$ git pull origin branch1
```

# git push

```shell
# 把本地仓库推送到远程仓库（默认主分支）
$ git push

# 把本地仓库推送到远程仓库的指定分支
$ git push <远程仓库> <远程分支>
$ git push origin branch1
```

# git status

```shell
# 显示工作目录和暂存区的状态。
$ git status
```

