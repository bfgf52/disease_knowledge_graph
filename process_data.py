import csv
import hashlib
import os
import re

from collections import defaultdict


def get_md5(string):
    """Get md5 according to the string
    """
    byte_string = string.encode("utf-8")
    md5 = hashlib.md5()
    md5.update(byte_string)
    result = md5.hexdigest()
    return result


dir_path = '.\中文糖尿病标注数据集'
file_names = os.listdir(dir_path)

entity_list = ['Symptom', 'Operation', 'Frequency', 'Drug', 'Test', 'Duration', 'Amount', 'Treatment', 'Anatomy', 'SideEff', 'Level', 'Disease', 'Method', 'Test_Value', 'Reason']

relation_list = ['Test_Disease', 'Treatment_Disease', 'Anatomy_Disease', 'Method_Drug', 'SideEff-Drug', 'Drug_Disease', 'Frequency_Drug', 'Symptom_Disease', 'Amount_Drug', 'Duration_Drug']

entity_dict = defaultdict(set)

relation_dict= defaultdict(list)


for file in file_names:
    if file.endswith('ann'):
        with open(os.path.join(dir_path,file),'r',encoding='utf-8') as f:
            t_name_dict = {}
            for line in f.readlines():
                item_list = line.split('\t')
                item0 = item_list[0]
                item1 = item_list[1].split()[0]
                if item0.startswith('T'):
                    item2 = re.sub(' ','',item_list[2]).strip()
                    entity_dict[item1].add(item2)
                    t_name_dict[item0] = item2
                else:
                    relation,arg1,arg2 = item_list[1].split()
                    arg1 = re.sub('Arg1:','',arg1)
                    arg2 = re.sub('Arg2:','',arg2)
                    relation_dict[relation].append([t_name_dict[arg1],t_name_dict[arg2]])

for entity,value in entity_dict.items():
    with open(os.path.join('.\import',entity.lower()+'.csv'),'w', encoding='utf-8',newline='') as f:
        writer = csv.writer(f, delimiter=',')
        headers = ['{}_id:ID'.format(entity.lower()), 'name', ':LABEL']
        writer.writerow(headers)
        for v in value:
            info = [get_md5(v),v,entity.lower()]
            writer.writerow(info)



for relation,value in relation_dict.items():
    if relation == 'Test_Disease':
        with open(os.path.join('.\import','test_disease.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            test_disease_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'test_of']
                if info not in test_disease_list:
                    test_disease_list.append(info)
                    writer.writerow(info)
    elif relation == 'Treatment_Disease':
        with open(os.path.join('.\import','treatment_disease.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            treatment_disease_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'treatment_of']
                if info not in treatment_disease_list:
                    treatment_disease_list.append(info)
                    writer.writerow(info)
    elif relation == 'Anatomy_Disease':
        with open(os.path.join('.\import','anatomy_disease.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            anatomy_disease_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'anatomy_of']
                if info not in anatomy_disease_list:
                    anatomy_disease_list.append(info)
                    writer.writerow(info)
    elif relation == 'Method_Drug':
        with open(os.path.join('.\import','method_drug.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            method_drug_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'method_of']
                if info not in method_drug_list:
                    method_drug_list.append(info)
                    writer.writerow(info)
    elif relation == 'SideEff-Drug':
        with open(os.path.join('.\import','sideeff-drug.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            sideeff_drug_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'sideeff_of']
                if info not in sideeff_drug_list:
                    sideeff_drug_list.append(info)
                    writer.writerow(info)
    elif relation == 'Drug_Disease':
        with open(os.path.join('.\import','drug_disease.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            drug_disease_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'drug_of']
                if info not in drug_disease_list:
                    drug_disease_list.append(info)
                    writer.writerow(info)
    elif relation == 'Frequency_Drug':
        with open(os.path.join('.\import','frequency_drug.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            frequency_drug_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'frequency_of']
                if info not in frequency_drug_list:
                    frequency_drug_list.append(info)
                    writer.writerow(info)
    elif relation == 'Symptom_Disease':
        with open(os.path.join('.\import','symptom_disease.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            frequency_drug_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'symptom_of']
                if info not in frequency_drug_list:
                    frequency_drug_list.append(info)
                    writer.writerow(info)
    elif relation == 'Amount_Drug':
        with open(os.path.join('.\import','amount_drug.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            amount_drug_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'amount_of']
                if info not in amount_drug_list:
                    amount_drug_list.append(info)
                    writer.writerow(info)
    elif relation == 'Duration_Drug':
        with open(os.path.join('.\import','duration_drug.csv'),'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            headers = [':START_ID', ':END_ID', ':TYPE']
            writer.writerow(headers)
            duration_drug_list = []
            for v in value:
                info = [get_md5(v[0]),get_md5(v[1]),'duration_of']
                if info not in duration_drug_list:
                    duration_drug_list.append(info)
                    writer.writerow(info)