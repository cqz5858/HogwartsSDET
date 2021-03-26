##项目介绍 该项目主要是记录了从霍格沃兹学院学习【测试开发】过程中进行的相关练习和实战

##作业地址 https://github.com/cqz5858/HogwartsStudy 参考代码地址：https://github.com/ceshiren/HogwartsSDET17

##git
霍格沃兹学院gitHub链接：https://github.com/ceshiren
作者gitHub链接：https://github.com/jumper0419
git教程：https://www.liaoxuefeng.com/wiki/896043488029600
git最全命令：https://ceshiren.com/t/topic/7405

##pytest
pytest使用文档：https://docs.pytest.org/en/latest/

数据驱动--yaml:
yaml使用文档说明：https://yaml.org/spec/1.2/spec.html
yaml使用：
yaml.safe_load(open('./xxx.yml'))

pytest命名规范：
测试用例命名规范:
文件要在test_开头，或者_test结尾
类要以Test开头，方法要以test_开头
常用参数
pytest --collect-only：只收集用例
pytest -k “add or test_b”: 匹配所有名称中包含add的用例（‘add or div’ ‘TestClass’）
pytest -m mark标签名: 标记
@pytest.mark.login函数被标记
fix pytest mark_warning:在pytest.ini中配置markers
pytest - - junitxml=./result.xml：生成执行结果文件
配合allure生成好看的测试报告
pytest --setup-show：回溯fixture的执行过程

##元素定位
img.png

##python
命名规范：https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id16
##selenium
selenium使用文档：https://selenium-python.readthedocs.io
测试人论坛 参考链接 pytest: https://docs.pytest.org/en/stable/getting-started.html
