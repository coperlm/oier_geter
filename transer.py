import re

def truncate_after_substring(input_str, substring):
    # 查找子字符串的位置
    pos = input_str.find(substring)
    if pos != -1:
        # 截取子字符串之前的部分
        return input_str[:pos]
    return input_str  # 如果子字符串未找到，返回原字符串
def truncate_before_substring(input_str, substring):
    # 查找子字符串的位置
    pos = input_str.find(substring)
    if pos != -1:
        # 截取子字符串及其后面的部分
        return input_str[pos:]
    return input_str  # 如果子字符串未找到，返回原字符串

def remove_second_last_char(input_str):
    if len(input_str) < 2:
        # 如果字符串长度小于2，则无法删除倒数第二个字符
        return input_str
    # 使用切片去掉倒数第二个字符
    return input_str[:-2] + input_str[-1]

def replace_multiple(input_str):
    replacements = ['>','<','\"','=','是中国信息学竞赛选手的一个数据库。你能够在这个网站上查询选手们的获奖记录，目前可以通过姓名、姓名首字母缩写、省份、年级和学校来进行查询','5241760357017591340297686','\'','\\','/',':--8-,-1是中国信息学竞赛选手的一个数据库。你能够在这个网站上查询选手们的获奖记录，目前可以通过姓名、姓名首字母缩写、省份、年级和学校来进行查询。;--180180--3232-32321616-1616---#888-#888-#:-2411820-1820-530-621---621---16131--:075;-:20;-首页-选手-学校-比赛-关于__32_14__4_1-搜索4-:1;:;-:-;0高级搜索','15;#姓名省份年级评分评级__19_','--8-,-1。;--180180--3232-32321616-1616---#888-#888-#:-2411820-1820-530-621---621---16131-83316704619051626494297733075825990396232237156307059872751894157217627739201386-:075;-:20;']
    # `replacements` 是一个字典，其中键是要替换的字符，值是替换后的字符
    for old in replacements:
        input_str = input_str.replace(old, "")
    input_str = truncate_after_substring(input_str,'___1-') + '\n'
    input_str = truncate_before_substring(input_str,'_19_').replace('_19_',' ').replace('_','\n')
    input_str = remove_second_last_char(input_str)
    return input_str

# 示例


def remove_letters(input_str):
    # 使用正则表达式删除所有字母（大小写）
    cleaned_str = re.sub(r'[a-zA-Z]', '', input_str).replace("键入学生姓名或其拼音首字母","").replace(" ","")
    cleaned_str = replace_multiple(cleaned_str)
    return cleaned_str

# 读取input.txt并写入output.txt
def read_and_write_file(input_file, output_file):
    try:
        # 打开输入文件并按行读取
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        # 打开输出文件并写入
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in lines:
                if 'no info' in line:
                    continue
                else:
                    t = remove_letters(line)
                    outfile.write(t)
        
        print(f"内容已成功从 {input_file} 写入到 {output_file} 中")
    
    except Exception as e:
        print(f"发生错误: {e}")

# 调用函数
input_file = 'input.txt'
output_file = 'output.txt'
read_and_write_file(input_file, output_file)
