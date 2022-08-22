# 1. 调用我的读取函数，读取data目录里的所有文件
import analyze
all = analyze.read_all()


# 2.调用结巴分词例子中的改造好的函数，来帮我们分词
import jieba_test
jieba_test.creat(all)