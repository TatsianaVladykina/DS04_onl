"""
Модуль для создания датафрейма с масками изображений, созданных в
LabelImg. Записывает пандас датафрейм в csv-файл.
"""
import os
import glob
import shutil
import xml.etree.ElementTree as ET
import pandas as pd


def xml_to_csv(path):
    """
    Фукнция для создания датафрейма с масками изображений, созданных в
    LabelImg. Принимает на вход путь до папки с .xml файлами.
    Возвращает пандас датафрейм.
    """
    xml_list = []

    for xml_file in glob.glob(path + '/*.xml'):

        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'clas', 'xmin', 'ymin', 'xmax', 'ymax']
    return pd.DataFrame(xml_list, columns=column_name)

if __name__ == '__main__':
    if not os.path.exists(os.getcwd() + '/masks'):
        shutil.unpack_archive(os.getcwd() + '/masks.zip')

    image_path = os.getcwd() + '/masks'
    df_xml = xml_to_csv(image_path)

    if os.path.exists(os.getcwd() + '/masks'):
        shutil.rmtree(os.getcwd() + '/masks')

    df_xml.sort_values(by=['filename'], inplace=True)
    df_xml.to_csv('Annotated_.csv', index=None)
    print('Successfully converted xml to csv.', df_xml.shape[0])
