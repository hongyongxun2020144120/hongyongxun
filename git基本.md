# **git基本原理**

-  Git工作区： 

1.  Remote： 远程仓库，托管代码的服务器（类似github）
2.   Repository：仓库区，也就是本地仓库（.git文件夹），安全存放数据的位置，里面有提交所有版本的数据，其中HEAD指向最新放入仓库的版本；
3.  index/Stage：暂存区，用于临时存放改动，实际上是一个文件，用于保存即将提交到文件列表的信息；
4.  workspace：工作区，也就是编辑文件的位置；

-  *****根据下图理解提交代码的流程：*

![](54d09f71-c7ae-4ed8-bb60-7f1bff80ecfa_2.png)

1.  git add：将工作区的文件提交到暂存区；
2.  git commit：将暂存区的文件提交到本地仓库；
3.  git push：将本地仓库提交到远程仓库；

-  *****Git文件状态：*

1.  **Untracked**：未跟踪，在此文件夹中，但没有加到git库，不参与版本控制，通过git add状态变为staged；
2.  **Unmodified**：文件已经入库，未修改，即版本库中的文件快照内容与文件夹一致这种类型的文件有两种取出，如果被修改，变为modified，如果被移除版本库git rm，变为Untracked；
3.   **Modified**：文件已被修改，这个文件有两个去处，第一个是staged，第二个是unmodified；
4.  **Staged**：执行git commit 则将修改同步到库中，这时库中的文件和本地文件虽为一致，文件为Unmodified。执行git reset HEAD filename取消暂存，文件状态为modified。![](4896b42c-d7e5-4771-a9e8-dad06b214be3_2.png)

-  *****git工作原理：*

1.  克隆Git资源作为工作目录
2.  在克隆的资源上添加或修改文件
3.  如果他人修改了，你可以更新资源
4.  在提交前查看修改
5.  提交修改
6.  在修改完成后，如果发现错误，可以撤回提交并再次修改并提交
7.  下图展示了Git的工作流程：![](9e862239-ea69-45d9-9a18-f4ced449f879_2.png)



# **基本使用：**

-  *****创建版本库*

> 什么是版本库？版本库又名仓库，英文名repository,你可以简单的理解一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改，删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻还可以将文件”还原”。（此时创建的版本库是 testTwo）

![](9ea913ae-e8f8-4775-9c1f-db1d264e2da5_2.png)mkdir新建一个目录，cd打开此目录，pwd查看此目录路径



----

-  *****通过命令 git init 把这个目录变成git可以管理的仓库*

> ![](0d4ef2b1-597d-40eb-980a-19386b3b5244_2.png)这时会在testTwo目录中生成一个.git（没出现可能是隐藏了）文件夹



----

-  *****git add 添加 与git committ提交*



> 举个小例子：
> 在版本库testTwo目录下新建一个test1.txt 文档 内容如下：11111
> 第一步：使用命令 git add test1.txt添加到暂存区里面去。（git add . 提交全部）
> 第二步：用命令 git commit -m 文件提交到仓库。(注意 -m 后面是提交时添加的注释)
> 第三步：用命令 git status来查看是否还有文件未提交。
> 第四步：用命令 git pull 更新 （命令用于从远程获取代码并合并本地的版本）。
> 第五步：用命令 git push 推送到远程仓库。
> 版权声明：本文为CSDN博主「Echo-潔」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
> 原文链接：[https://blog.csdn.net/qq\_44094296/article/details/114324505](https://blog.csdn.net/qq_44094296/article/details/114324505)



----

-  *****git diff使用*

> 在test1.txt中添加内容22222，没有进行git add add/or git commit 操作,也就是说修改后的test1.txt 还在工作区。这时执行git status 它会提示 modified：test1.txt，意思是说，有一个修改的文件未提交。可以用 cat test1.txt 查看文件内容 。（重点） 在未提交的情况下 git diff 可以查看修改了什么内容
> 
> 如果执行了git add，则如下图
> 版权声明：本文为CSDN博主「Echo-潔」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
> 原文链接：[https://blog.csdn.net/qq\_44094296/article/details/114324505](https://blog.csdn.net/qq_44094296/article/details/114324505)



----

-  *****版本回避*

> 查看历史记录 git log， git log – –pretty=oneline信息简化
> 
> 版本回退：
> 第一种：git reset --hard HEAD^ ，如果要回退到上上个版本只需把HEAD^ 改成 HEAD^^ 以此类推，如果回退到更久的版本则命令操作：git reset --hard HEAD~100
> 如下图展示：
> 
> 第二种：通过版本号回退 git reset --hard 版本号。获取版本号：git reflog
> 如下图所示：
> 版权声明：本文为CSDN博主「Echo-潔」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
> 原文链接：[https://blog.csdn.net/qq\_44094296/article/details/114324505](https://blog.csdn.net/qq_44094296/article/details/114324505)



----

-  *****Git撤销修改和删除文件操作*

> **撤销：** git checkout – file 可以撤销某个文件在工作区的修改

![](b4813c38-f6da-4f08-98cb-e32ef26be22d_2.png)

**删除：** rm 文件，看下图：

![](30e4940a-9636-431f-aab9-eede71fff86f_2.png)

