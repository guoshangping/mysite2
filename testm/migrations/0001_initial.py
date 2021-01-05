# Generated by Django 2.1.8 on 2020-12-28 10:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_index', models.CharField(blank=True, max_length=20, verbose_name='通过性')),
                ('evaluate_index', models.CharField(blank=True, max_length=200, verbose_name='评价性')),
            ],
            options={
                'verbose_name': '测试报告|产品测试结论',
                'verbose_name_plural': '测试报告|产品测试结论',
                'db_table': 'conclusion_t',
            },
        ),
        migrations.CreateModel(
            name='Dongtai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='操作时间')),
                ('operation', models.CharField(max_length=200, verbose_name='操作进度')),
            ],
        ),
        migrations.CreateModel(
            name='Executes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execute_name', models.CharField(max_length=20, verbose_name='实施阶段')),
                ('responsible_party', models.CharField(max_length=20, verbose_name='责任方')),
                ('start_time', models.DateField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end_time', models.DateField(default=django.utils.timezone.now, verbose_name='结束时间')),
                ('execute_description', models.CharField(max_length=200, verbose_name='实施描述')),
            ],
            options={
                'verbose_name': '测试报告|实施时间',
                'verbose_name_plural': '测试报告|实施时间',
                'db_table': 'executes_t',
            },
        ),
        migrations.CreateModel(
            name='Pro_speed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed_name', models.CharField(max_length=30, verbose_name='项目进度')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('project_name', models.CharField(max_length=20, verbose_name='项目名称')),
                ('meeting_status', models.CharField(blank=True, default='0', max_length=20, null=True, verbose_name='上会状态')),
            ],
            options={
                'verbose_name': '测试项目',
                'verbose_name_plural': '测试项目',
                'db_table': 'projects_t',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=200, verbose_name='报告名称')),
                ('test_background', models.TextField(blank=True, verbose_name='测试背景')),
                ('test_object', models.TextField(blank=True, verbose_name='测试对象')),
                ('test_demand', models.FileField(blank=True, upload_to='upload', verbose_name='需求文档')),
                ('pass_index', models.FileField(blank=True, upload_to='upload', verbose_name='通过性文档')),
                ('evaluate_index', models.FileField(blank=True, upload_to='upload', verbose_name='评价性文档')),
                ('test_case', models.FileField(blank=True, upload_to='upload', verbose_name='测试案例')),
                ('organization_framework', models.TextField(default='    本次测试由财务会计部采购部牵头成立选型测试小组，相关组织机构职责如下：\r    【选型组织】财务会计部采购部负责选型测试工作的牵头组织，负责测试计划推进以及参测单位之间的问题、资源协调。\r    【选型需求（管理）部门】XXXX负责提出选型测试需求；参与产品调研、测试案例编写和选型测试工作；参与选型测试实施过程管理；参与测试报告的汇总、编写。\r    【选型测试单位】XXXX负责协助提出选型测试需求；负责编写测试方案、测试计划、测试用例及测试需要的其他技术资料；负责进行选型需求分析和调研；负责选型的具体实施，记录和保存测试过程数据；组织起草选型测试报告；负责保管选型测试样品、录音录像和过程资料。', verbose_name='组织架构')),
                ('test_location', models.CharField(blank=True, max_length=200, verbose_name='测试地点')),
                ('test_flow', models.TextField(blank=True, default='    采购部组织召开选型测试启动会，候选选型供应商代表签到，学习测试工作纪律，提交测试文件并进行测试顺序抽签。\r    候选选型供应商按照抽签次序分成两组进行测试。每家供应商只能推荐1个型号的设备进行测试，原则上每家供应商测试时间为1天。\r    按照抽签次序，首先由供应商人员负责安装调试，时间为30分钟左右，在安装调试过程中可以更换机具，供应商授权代表确认可以开始测试后，不再允许更换备件或整机。\r    供应商授权代表确认可以开始测试后，供应商测试操作员进行测试操作，每测试一个用例，建行测试记录员当场记录测试结果，测试结果由建行人员及供应商授权代表共同签字确认。对于测试结果描述的涂改，需测试记录员与供应商授权代表共同签名，并注明涂改原因。', verbose_name='测试流程')),
                ('test_environment', models.TextField(blank=True, verbose_name='测试环境')),
                ('test_records', models.TextField(blank=True, verbose_name='测试记录')),
                ('test_results', models.TextField(blank=True, verbose_name='测试结果')),
            ],
            options={
                'verbose_name': '测试报告',
                'verbose_name_plural': '测试报告',
                'db_table': 'reports_t',
            },
        ),
        migrations.CreateModel(
            name='Reports_groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='姓名')),
                ('department', models.CharField(blank=True, max_length=200, verbose_name='部门')),
                ('contacts', models.CharField(blank=True, max_length=20, verbose_name='联系方式')),
                ('responsibilities', models.CharField(blank=True, max_length=200, verbose_name='职责')),
                ('group_flag', models.IntegerField(choices=[(0, '协助组'), (1, '作业组')], default=0, verbose_name='组标识')),
            ],
            options={
                'verbose_name': '测试报告|小组组成',
                'verbose_name_plural': '测试报告|小组组成',
                'db_table': 'groups_t',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '打分工具',
                'verbose_name_plural': '打分工具',
            },
        ),
        migrations.CreateModel(
            name='Sp_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('e_time', models.DateTimeField(default='2020-12-31 01:01:01', verbose_name='结束时间')),
                ('status', models.CharField(default='未启动', max_length=30, verbose_name='状态')),
                ('name', models.CharField(default='', max_length=30, verbose_name='项目名称')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('test_date', models.CharField(default='_____年___月___日', max_length=20, verbose_name='测试时间')),
                ('test_location', models.CharField(choices=[('YQ', '洋桥'), ('DXH', '稻香湖')], default='YQ', max_length=10, verbose_name='测试地点')),
                ('prod_name', models.CharField(default='', max_length=20, verbose_name='产品名')),
                ('vend_name', models.CharField(default='', max_length=20, verbose_name='供应商')),
                ('test_purpose', models.TextField(verbose_name='测试目的')),
                ('test_design', models.TextField(verbose_name='测试设计')),
                ('test_conditions', models.TextField(verbose_name='测试条件')),
                ('test_procedure', models.TextField(verbose_name='测试步骤')),
                ('expected_results', models.TextField(verbose_name='预期结果')),
                ('test_result', models.TextField(default='□通过  □部分通过  □未通过  □未测试', verbose_name='测试结果')),
                ('sign', models.TextField(default='测试人员____________________       供应商______________________', verbose_name='签名')),
                ('remark', models.TextField(default='“通过”需满足全部要求', verbose_name='备注')),
            ],
            options={
                'verbose_name': '测试案例',
                'verbose_name_plural': '测试案例',
                'db_table': 'case_t',
            },
        ),
    ]
