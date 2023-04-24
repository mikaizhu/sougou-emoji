# 我的搜狗(sougou)自定义词库

💻**使用环境:**
- Mac OS

⚙**操作方法：**
1. 将`phrases.ini`文件下载到你的电脑上

2. 在搜狗输入法中，"偏好设置-高级-自定义短语-导入"

3. 再选择`phrases.ini`导入

# 常见问题
🤔：这是我在导入emoji文件遇到的问题，希望可以对你自己导入自定义短语有所帮助。

❓问题1：搜狗输入法导入文件显示"文件错误，导入失败"

💡：
1. 注意后缀为`ini`，我通过`transfer_to_sougou.py` 代码，将参考项目2中的rime格式的pinyin to emoji文件，转换成了搜狗格式文件`pinyin-sougou-emoji.txt`，将文件改成ini后缀格式`pinyin-sougou-emoji.ini`
2. 注意搜狗自定义短语的格式为`abc,2=emoji`，左边abc部分不能出现空格，2为该表情出现的位置，我设置为4，防止一些常用词语被emoji占用，按照上面操作方法，对`pinyin-emoji.ini`文件进行导入时，出现了“文件错误，导入失败”问题, 于是我尝试自己添加一些常用短语，并且将这些短语进行导出，获得了`phrases.ini`文件。并发现该文件是可以被导入的，于是我将`pinyin-emoji.ini`中的所有emoji，复制到`phrases.ini`中进行导入，于是导入成功。

❓问题2：windows电脑如何导入自定义短语emoji？

💡：
1. 可以参考项目1

❓问题3：如何导入双拼的自定义短语emoji？

💡：
1. 可以参考项目3

# 👏🏻提供建议
欢迎提供更好的pinyin-emoji的映射文件，非常感谢☺️！

我查看了`pinyn-sougou-emoji.ini`格式，与导出的`phrases.ini`格式相同，但前者会出现导入错误，不清楚什么问题，如果你知道原因，可以提出issue

# 参考
1.  [GitHub - U1805/Sogou-emoji-thesaurus: 搜狗emoji自定义词库](https://github.com/U1805/Sogou-emoji-thesaurus)
2.  [Pinyin-Emoji Dictionary for Squirrel · GitHub](https://gist.github.com/lembacon/4593540)
3. [GitHub - yuhangch/zhmoji: 用作搜狗拼音自定义短语，输入😄而不是图片。](https://github.com/yuhangch/zhmoji)
