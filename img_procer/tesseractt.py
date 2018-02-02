import os
import subprocess


def image_to_string(img, lang='chi_sim', cleanup=False, plus=''):
    """
    与shell互动获得ocr结果
    :param img: 文件名
    :param lang: 语言，默认为简体中文——chi_sim
    :param cleanup: 识别完成后删除生成的文本文件
    :param plus: 高级参数
    :return: ocr结果
    """
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    subprocess.check_output('tesseract "' + img + '" "' +
                            img + '" -l ' + lang + ' ' + plus, shell=True)  # 生成同名txt文件

    text = ''
    with open(img + '.txt', 'r', encoding='utf-8') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text
