# 读取input.txt并写入output.txt
def read_and_write_file(input_file, output_file):
    try:
        # 打开输入文件并按行读取
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        # 打开输出文件并写入
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in lines:
                if '高中毕业1年' in line:
                    startt = 0
                    for i in line:
                        if (i <= '9' and i >= '0') or i == ' ':
                            startt += 1
                        else:
                            break
                    line = "CCF评级：" + line[len(line)-2:len(line)-1] + "  | 谁这么厉害：" + line[startt:len(line)-2] + '\n'
                    outfile.write(line)
        
        print(f"内容已成功从 {input_file} 写入到 {output_file} 中")
    
    except Exception as e:
        print(f"发生错误: {e}")

# 调用函数
input_file = 'output.txt'
output_file = 'endd.txt'
read_and_write_file(input_file, output_file)
