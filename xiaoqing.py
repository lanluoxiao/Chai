from Chai import Erbi

# 方案未完成！请先不要运行该文件。
xiaoqing = Erbi('xiaoqing')
xiaoqing.run()

for nameChar in xiaoqing.charList:
    if nameChar in xiaoqing.component:
        # 如果字是基本部件，则获取字根拆分
        root, strokeList = xiaoqing.component[nameChar]
        scheme = [root] + strokeList[-1:] * 4
    else:
        # 否则先按嵌套拆分拆开对于拆出的每个基础字，索引出其用户字根拆分列，最后组合起来
        tree = xiaoqing.tree[nameChar]
        first = tree.first
        second = tree.second
        if second.divisible():
            r1, sl1 = xiaoqing.component[first.veryFirst()]
            r2, sl2 = xiaoqing.component[second.first.veryFirst()]
            r3, sl3 = xiaoqing.component[second.second.veryFirst()]
            scheme = [r1] + [sl2[0], sl2[-1], sl3[0], sl3[-1]]
        elif first.divisible():
            r1, sl1 = xiaoqing.component[first.first.veryFirst()]
            r2, sl2 = xiaoqing.component[second.first.veryFirst()]
            r3, sl3 = xiaoqing.component[second.second.veryFirst()]
            scheme = [r1] + [sl2[0], sl2[-1], sl3[0], sl3[-1]]
        else:
            r1, sl1 = xiaoqing.component[first]
            r2, sl2 = xiaoqing.component[first]
            scheme = [r1] + sl2[:3] + sl2[-1:]
    code = ''.join(xiaoqing.rootSet[root] for root in scheme)
    xiaoqing.encoder[nameChar] = code

xiaoqing.output()