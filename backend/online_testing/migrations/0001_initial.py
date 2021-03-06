# Generated by Django 2.0.5 on 2018-06-01 02:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import online_testing.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('exam_id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, verbose_name='考试号')),
                ('answers', models.TextField(default=None, null=True, verbose_name='答案')),
                ('score', models.SmallIntegerField(default=-1, verbose_name='分数')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('submit', models.BooleanField(default=False, verbose_name='提交状态')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('paper_id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, verbose_name='试卷ID号')),
                ('paper_name', models.CharField(max_length=128, verbose_name='试卷名')),
                ('start_time', models.DateTimeField(default=datetime.datetime(2018, 6, 1, 2, 39, 35, 788414, tzinfo=utc), verbose_name='开始时间')),
                ('deadline', models.DateTimeField(default=datetime.datetime(2018, 6, 1, 2, 39, 35, 788414, tzinfo=utc), verbose_name='结束时间')),
                ('duration', models.IntegerField(verbose_name='持续时间(分)')),
                ('score_list', online_testing.models.ListField(verbose_name='分数表')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Course', verbose_name='所属课程')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False, verbose_name='问题ID号')),
                ('description', models.TextField(verbose_name='问题描述')),
                ('choice_list', online_testing.models.ListField(verbose_name='选择')),
                ('answer_list', online_testing.models.ListField(verbose_name='答案')),
                ('tag', models.CharField(max_length=32, verbose_name='标签')),
                ('type', models.CharField(choices=[('Choice', 'Choice'), ('Judge', 'Judge')], default='Choice', max_length=12, verbose_name='问题类型')),
                ('level', models.IntegerField(choices=[(0, 'Very Easy'), (1, 'Easy'), (2, 'Medium'), (3, 'Difficult'), (4, 'Very Difficult')], default=0, verbose_name='问题难度')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Course', verbose_name='所属课程')),
                ('provider', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Faculty', verbose_name='出题人')),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='question_id_list',
            field=models.ManyToManyField(related_name='问题', to='online_testing.Question'),
        ),
        migrations.AddField(
            model_name='paper',
            name='teacher',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Faculty', verbose_name='布置人'),
        ),
        migrations.AddField(
            model_name='examination',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_testing.Paper', verbose_name='试卷'),
        ),
        migrations.AddField(
            model_name='examination',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Student', verbose_name='学生'),
        ),
    ]
