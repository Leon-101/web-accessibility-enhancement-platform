from django.db import models


# Create your models here.
class User(models.Model):
    """用户表"""
    username = models.CharField(verbose_name="用户名", max_length=32, primary_key=True)
    password = models.CharField(verbose_name="密码", max_length=32)
    email = models.EmailField(verbose_name="邮箱", null=True, blank=True)
    role = models.ForeignKey(to="Role", to_field="id", null=True, blank=True, on_delete=models.SET_NULL, default=1)
    # whatsup = models.CharField(max_length=100, null=True, blank=True)


class Role(models.Model):
    """角色表"""
    name = models.CharField(verbose_name="角色名称", max_length=8)


class Script(models.Model):
    id = models.CharField(verbose_name="脚本ID", max_length=32, primary_key=True)
    title = models.CharField(verbose_name="标题", max_length=32)
    description = models.CharField(verbose_name="描述", max_length=100, null=True, blank=True)
    author = models.ForeignKey(verbose_name="作者", to='User', to_field="username", null=True, blank=True,
                               on_delete=models.SET_NULL)
    status = models.ForeignKey(verbose_name="状态", to='Status', to_field="id", null=True, blank=True,
                               on_delete=models.SET_NULL)
    create_time = models.DateTimeField(verbose_name="创建时间")
    download_count = models.IntegerField(verbose_name="下载次数", default=0)
    stars = models.IntegerField(verbose_name="收藏/星标数", default=0)
    script_path = models.CharField(verbose_name="脚本文件路径", max_length=200)
    readme = models.TextField(verbose_name="脚本的说明文档", null=True, blank=True)


class Status(models.Model):
    """脚本状态"""
    status = models.CharField(verbose_name="状态", max_length=8)


class Permission(models.Model):
    """权限表"""
    pass


class RolePermission(models.Model):
    """角色和权限表"""
    pass


class Comment(models.Model):
    """评论表"""
    pass


class Task(models.Model):
    """任务 / 需求表"""
    pass


class Operation(models.Model):
    """操作记录"""
    op_name = models.CharField(verbose_name="操作名称", max_length=8)


class UserOperation(models.Model):
    """用户操作记录"""
    # 这里全部采用级联删除
    script = models.ForeignKey(to="Script", to_field="id", on_delete=models.CASCADE)
    user = models.ForeignKey(to="User", to_field="username", on_delete=models.CASCADE)
    op = models.ForeignKey(to="Operation", to_field="id", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="操作时间")


class Website(models.Model):
    """网页表，
    记录已经有哪些网页的脚本了，以URL匹配的形式存
    """
    url = models.URLField(verbose_name="匹配的网址")
    description = models.CharField(verbose_name="描述", max_length=100)


class ScriptWebsite(models.Model):
    """脚本与应用网页关联表"""
    script = models.ForeignKey(to="Script", to_field="id", on_delete=models.CASCADE)
    website = models.ForeignKey(to="Website", to_field="id", on_delete=models.CASCADE)
