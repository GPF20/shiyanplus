##git--github
git #查看是否安装成功，内含git命令
##在github中添加一个仓库
mkdir Demo #新建仓库目录
git init #输入命令来进行git操作控制目录或文件
git add --all #将目录下所有文件添加到本地暂存区域 --all可换成文件名/目录名
git status #查看当前目录和暂存区的状态
git commit #提交你的工作/保持当前的版本
git config --global user.name "YourName"
git config --global user.email "YourEmail" #提交之前设置你的名字和email，每次提交都会包含这些信息
git commit -m "first commit" #注释，为你的git提交创建一条注释
git remote add origin http://... #将本地仓库连接Github仓库 origin是自取的小仓库名
git push origin master #推送你要上传的内容，origin小仓库名与上相同，master分支名
#回车后输入GitHub的用户名与密码，密码不可见输入后回车。
git clone link #将github的仓库克隆到当前目录下。


